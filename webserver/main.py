import os
import string
from datetime import datetime
from datetime import timedelta
from random import SystemRandom

import pymongo
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel

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
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


class Paste(BaseModel):
    expire: int = 1
    data: str


def generate_key(size=6) -> str:
    sr = SystemRandom()
    key = "".join(sr.choices(string.ascii_letters + string.digits, k=size))
    if collection.find_one({"key": key}):
        return generate_key(size=size + 1)
    return key


@app.post("/api", summary="Create new paste", status_code=status.HTTP_201_CREATED)
def api_create(paste: Paste) -> dict:
    key = generate_key()
    document: dict = paste.dict()
    document.update(key=key, timestamp=datetime.now())
    if paste.expire > 0:
        document.update(expire_at=datetime.now() + timedelta(days=paste.expire))
    collection.insert_one(document)
    return {"key": key}


@app.get("/api/{key}", summary="Retrieve a paste", status_code=status.HTTP_200_OK)
def api_get(key: str) -> dict:
    paste = collection.find_one({"key": str(key)}, {"_id": False, "data": True})
    if paste:
        return paste  # noqa
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paste not found")
