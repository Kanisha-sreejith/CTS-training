from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI Example")


class Item(BaseModel):
    name: str
    quantity: int


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@app.get("/items")
def list_items():
    return [{"name": "Book", "quantity": 2}, {"name": "Pen", "quantity": 5}]


@app.post("/items")
def create_item(item: Item):
    return {"message": "Created", "item": item}
