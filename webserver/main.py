import os
import pymongo
import time
import uuid
from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()
client = pymongo.MongoClient(os.getenv("DATABASE_URL", "mongodb://localhost:27017/"))
collection = client.get_database("sahibin").get_collection("paste")


class Paste(BaseModel):
    key: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: int = 0
    data: str


@app.post("/api/create", summary="Create new paste", status_code=status.HTTP_201_CREATED)
def api_create(paste: Paste) -> dict:
    if collection.find_one({"key": paste.key}):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"A paste with key {paste.key} already exists")
    paste.timestamp = int(datetime.now().timestamp() * 1000)
    collection.insert_one(paste.dict())
    return {"key": paste.key}


@app.get("/api/get", summary="Retrieve a paste", status_code=status.HTTP_200_OK)
def api_get(key: str) -> dict:
    paste = collection.find_one({"key": str(key)}, {"_id": False, "data": True})
    if paste:
        return paste  # noqa
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paste not found")


@app.get("/api/raw", summary="Retrieve a paste as raw", status_code=status.HTTP_200_OK)
def api_get_raw(key: str) -> Response:
    paste = collection.find_one({"key": str(key)}, {"_id": False, "data": True})
    if paste:
        return Response(content=paste.get("data"))
    return Response(content="Paste not found", status_code=status.HTTP_404_NOT_FOUND)
