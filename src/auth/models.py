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

    # def __dict__(self):
    #     return {
    #         "access_token": self.access_token,
    #         "token_type": self.token_type,
    #     }


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(BaseModel):
    ID: int
    Name: str
    Surname: str
    Nickname: str
    PasswordHash: int
    CreatedAt: int
    EditedAt: int
