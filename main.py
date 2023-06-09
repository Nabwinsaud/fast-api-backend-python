from typing import Union

from fastapi import FastAPI
from prisma import Prisma
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello : " "world"}


@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
