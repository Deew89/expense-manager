from fastapi import FastAPI, Query
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Define a Pydantic model for POST request data
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Simple GET route
@app.get("/hello")
def read_hello(name: str = Query("World", description="Who do you want to greet?")):
    return {"message": f"Hello, {name}!"}

# GET with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "Details about this item"}

# POST route that accepts JSON
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item received", "item": item}
