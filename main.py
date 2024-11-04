from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {
        "message": "Hello World"
    }

@app.get("/check")
async def check():
    return {
        "message": "application running"
    }
