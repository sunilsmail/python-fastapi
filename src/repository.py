from sqlalchemy.orm import Session
from . import models, schemas

class UserRepository:
    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate):
        new_user = models.User(name=user.name, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_all_users(db: Session):
        return db.query(models.User).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user_data: schemas.UserCreate):
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            user.name = user_data.name
            user.email = user_data.email
            db.commit()
            db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
