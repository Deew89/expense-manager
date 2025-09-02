from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app import models, database, security

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(database.get_db)):
    # Example logic
    user = db.query(models.User).filter(models.User.email == username).first()
    if not user or not security.verify_password(password, user.password_hash):
        return {"detail": "Invalid credentials"}
    token = security.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
