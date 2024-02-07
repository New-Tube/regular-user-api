from pydantic import BaseModel


class UserRegistrionRequest(BaseModel):
    username: str
    password: str
    name: str | None = None
    surname: str | None = None


class UserLoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class OAuthUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(UserRegistrionRequest):
    hashed_password: str
