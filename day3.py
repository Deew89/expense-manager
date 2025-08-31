from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import Expense
from pydantic import BaseModel
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str
    date: str

class ExpenseResponse(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True

@app.post("/expenses/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses/", response_model=List[ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()
