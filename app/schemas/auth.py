from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class UserLogin(BaseModel):
    username: str
    password: str
