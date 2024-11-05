from typing import Union
from fastapi import FastAPI
import uvicorn
from enum import Enum
from pydantic import BaseModel

app = FastAPI(
    title="py fastapi restful api crud",
    description="python 3.11 fastapi for create restful api CRUD",
    version="1.0.0",
    debug=True,
    summary="py fastapi restful crud"
)


# inventory management system
class Category(Enum):
    TOOLS = "tools"
    CONSUMABLE = "consumable"

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

# simple dictionary of some items
items = {
    0: Item(name="Hammer", price=9.99, count=20, id=1, category=Category.TOOLS),
    1: Item(name="Pliers", price=9.19, count=10, id=2, category=Category.TOOLS),
    2: Item(name="Nails", price=1.09, count=100, id=3, category=Category.CONSUMABLE)
}


# FastAPI handles JSON serialization and deserialization for us.
# we can simply use build-in python and Pydantic types, in this case dic[int,]
@app.get("/")
async def read_root():
    return {
        "message": "Hello World"
    }

@app.get(
    "/check",
    responses={
        200: {"description":"success response"}
    },
)
async def check():
    return {
        "message": "application running"
    }


@app.get("/api/v1/items")
def get_items() -> dict[str, dict[int, Item]]:
    return{
        "items": items
    }
