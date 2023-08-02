from typing import List
from uuid import uuid4

from fastapi import FastAPI
import os

from models import User
app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Slava",
         last_name="Nemo"),
    User(id=uuid4(),
         first_name="Anna",
         last_name="Mihno")
]


@app.get("/")
async def root():
    return {"message": f"{os.getenv('CLIENT_ID')}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello{name}"}


@app.get("/users")
async def get_users():
    return db
