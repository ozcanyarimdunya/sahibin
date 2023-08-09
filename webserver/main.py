import os
import re
import string
import tempfile
import time
import unicodedata
import zipfile
from datetime import datetime
from datetime import timedelta
from pathlib import Path
from random import SystemRandom

import pymongo
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pydantic import Field

os.environ.setdefault("TZ", "Europe/Istanbul")
time.tzset()
debug = os.getenv("MODE") == "DEV"
app = FastAPI(debug=debug)
client = pymongo.MongoClient(os.getenv("DATABASE_URL", "mongodb://localhost:27017/"))
collection = client.get_database("sahibin").get_collection("paste")
collection.create_index("expire_at", expireAfterSeconds=0)

if debug:
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["user-session-id"]
    )


class Paste(BaseModel):
    expire: int = 1
    data: str
    title: str = Field(None, max_length=50)


def generate_key(size=6) -> str:
    sr = SystemRandom()
    key = "".join(sr.choices(string.ascii_letters + string.digits, k=size))
    if collection.find_one({"key": key}):
        return generate_key(size=size + 1)
    return key


def normalize_text(text: str):
    text = text.strip()
    text = re.sub(r"[^\w.-]", "_", text)
    text = (
        unicodedata
        .normalize('NFKD', text)
        .encode('ascii', 'ignore')
        .decode('utf-8')
    )
    text = re.sub(r'_+', '_', text)
    return text


@app.middleware("http")
async def add_user_session_id(request: Request, call_next):
    response = await call_next(request)
    user_session = request.headers.get("user-session-id")
    if user_session:
        response.headers["user-session-id"] = user_session
    return response


@app.post("/api", summary="Create new paste", status_code=status.HTTP_201_CREATED)
def api_create(request: Request, paste: Paste) -> dict:
    key = generate_key()
    document: dict = paste.dict()
    document.update(
        key=key,
        timestamp=datetime.now(),
        userSessionId=request.headers.get("user-session-id"),
    )
    if paste.expire > 0:
        document.update(expire_at=datetime.now() + timedelta(days=paste.expire))
    collection.insert_one(document)
    return {"key": key}


@app.get("/api/history", summary="Retrieve user paste", status_code=status.HTTP_200_OK)
def api_history(request: Request, q: str = ""):
    pastes = (
        collection.find(
            {
                "userSessionId": {
                    "$eq": request.headers.get("user-session-id"),
                    "$exists": True,
                    "$ne": None,
                },
                "$or": [
                    {"data": {"$regex": q, "$options": "i"}},
                    {"title": {"$regex": q, "$options": "i"}},
                ],
            },
            {
                "_id": False,
                "key": True,
                "timestamp": True,
                "expire_at": True,
                "title": True,
                "views": True,
                "data": {
                    "$substr": ["$data", 0, 250]
                }
            }
        )
        .sort("timestamp", direction=pymongo.DESCENDING)
        .limit(50)
    )
    return list(pastes)


@app.get("/api/export", summary="Download user paste as zip", status_code=status.HTTP_200_OK)
def api_export(request: Request):
    pastes = (
        collection.find(
            {
                "userSessionId": {
                    "$eq": request.headers.get("user-session-id"),
                    "$exists": True,
                    "$ne": None,
                },
            },
            {
                "_id": False,
                "key": True,
                "title": True,
                "data": True
            }
        )
        .sort("timestamp", direction=pymongo.DESCENDING)
    )

    temp_dir = tempfile.mkdtemp(dir="/tmp")
    zip_path = Path(temp_dir) / "export.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for paste in pastes:
            text = paste.get("key", "") + "-" + paste.get("title", "")
            filename = normalize_text(text) + ".txt"
            temp_file_path = Path(temp_dir) / filename
            with temp_file_path.open(mode="w") as fp:
                fp.write(paste.get("data"))
            zipf.write(temp_file_path, arcname=filename)
    return FileResponse(zip_path, headers={"Content-Disposition": "attachment; filename=export.zip"})


@app.get("/api/{key}", summary="Retrieve a paste", status_code=status.HTTP_200_OK)
def api_get(key: str) -> dict:
    paste = collection.find_one_and_update(
        {"key": str(key)},
        {"$inc": {"views": 1}},
        {"_id": False, "data": True, "timestamp": True, "title": True, "expire": True, "views": True}
    )
    if paste:
        return paste  # noqa
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paste not found")


@app.patch("/api/{key}", summary="Edit a paste", status_code=status.HTTP_200_OK)
def api_edit(request: Request, key: str, paste: Paste) -> dict:
    found = collection.find_one(
        {
            "key": str(key),
            "userSessionId": {
                "$eq": request.headers.get("user-session-id"),
                "$exists": True,
                "$ne": None,
            }
        }
    )
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paste not found or you're not authorized to edit"
        )

    document: dict = paste.dict()

    if paste.expire <= 0:
        document.update(expire_at=None)
    else:
        document.update(expire_at=found["timestamp"] + timedelta(days=paste.expire))

    collection.update_one({'_id': found['_id']}, {"$set": document})
    return {"key": key}


@app.delete("/api/{key}", summary="Delete a paste", status_code=status.HTTP_204_NO_CONTENT)
def api_delete(request: Request, key: str):
    paste = collection.find_one_and_delete(
        {
            "key": str(key),
            "userSessionId": {
                "$eq": request.headers.get("user-session-id"),
                "$exists": True,
                "$ne": None,
            },
        },
        {
            "_id": False,
        }
    )
    if not paste:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paste not found or you're not authorized to delete"
        )
