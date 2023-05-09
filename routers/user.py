from typing import List

from services.user import UserService
from db.database import get_db
from api.schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return UserService.create_user(db, request)


# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db)


@router.get('/{user_id}', response_model=UserDisplay)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Article not found')
    return user


@router.patch('/{user_id}', response_model=UserDisplay)
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return UserService.update_user(db, user_id, request)


@router.delete('/{user_id}', response_model=None)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Article not found')
    return UserService.delete_user(db, user_id)
