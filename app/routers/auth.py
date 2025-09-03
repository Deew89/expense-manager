from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from app import models, database, security

router = APIRouter(tags=["auth"])

@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.email == username).first()
    if not user or not security.verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = security.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
