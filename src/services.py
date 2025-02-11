from sqlalchemy.orm import Session
from .repository import UserRepository
from .schemas import UserCreate

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        return UserRepository.create_user(db, user)

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_user(db, user_id)

    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all_users(db)

    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserCreate):
        return UserRepository.update_user(db, user_id, user_data)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        return UserRepository.delete_user(db, user_id)
