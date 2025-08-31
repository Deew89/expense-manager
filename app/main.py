from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    
@app.get("/hello")
def say_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items")
def create_item(item: Item):
    return {"received_item": item}