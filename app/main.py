from fastapi import FastAPI
from app.routers import users, auth

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Welcome to Expense Manager API"}
