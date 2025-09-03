from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, models
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/me", response_model=schemas.UserResponse )
def read_users_me(
    current_user: models.User = Depends(get_current_user),
):
    return current_user