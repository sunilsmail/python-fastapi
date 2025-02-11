from pydantic import BaseModel, EmailStr

# Request schema (used for input validation)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Response schema (used to serialize output)
class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True
