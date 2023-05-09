from typing import List, Type

from sqlalchemy.orm.session import Session

from db.hash import Hash
from api.schemas import UserBase
from db.models import DbUser


class UserService:
    @classmethod
    def create_user(cls, db: Session, request: UserBase) -> DbUser:
        new_user = DbUser(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @classmethod
    def get_all_users(cls, db: Session) -> List[Type[DbUser]]:
        return db.query(DbUser).all()

    @classmethod
    def get_user(cls, db: Session, user_id: int) -> Type[DbUser]:
        return db.query(DbUser).filter(DbUser.id == user_id).first()

    @classmethod
    def update_user(cls, db: Session, user_id: int, request_body: UserBase) -> Type[DbUser]:
        user = db.query(DbUser).filter(DbUser.id == user_id)
        user.update({
            DbUser.username: request_body.username,
            DbUser.email: request_body.email,
            DbUser.password: Hash.bcrypt(request_body.password),
        })
        db.commit()
        return user.first()

    @classmethod
    def delete_user(cls, db: Session, user_id: int):
        user = cls.get_user(db, user_id)
        db.delete(user)
        db.commit()
