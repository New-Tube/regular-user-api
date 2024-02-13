import pydantic


class UserRegistrionRequest(pydantic.BaseModel):
    username: str
    password: str
    name: str | None = None
    surname: str | None = None

    @pydantic.field_validator("username")
    @classmethod
    def check_username(cls, v: str, info: pydantic.ValidationInfo) -> str:
        assert isinstance(v, str), f"{info.field_name} is not a string"
        assert v.isascii(), f"{info.field_name} must be ascii"
        assert 4 < len(v) < 40, f"{info.field_name} len must be > 4 and < 40"
        assert not v.isnumeric(), (
            f"{info.field_name} must ",
            "contain non numeric symbols",
        )
        return v

    @pydantic.field_validator("username")
    @classmethod
    def check_password(cls, v: str, info: pydantic.ValidationInfo) -> str:
        assert isinstance(v, str), f"{info.field_name} is not a string"
        assert v.isascii(), f"{info.field_name} must be ascii"
        assert 4 < len(v) < 100, f"{info.field_name} len must be > 4 and < 100"
        assert not v.isnumeric(), (
            f"{info.field_name} must ",
            "contain non numeric symbols",
        )
        return v


class UserLoginRequest(pydantic.BaseModel):
    username: str
    password: str


class Token(pydantic.BaseModel):
    access_token: str
    token_type: str

    # def __dict__(self):
    #     return {
    #         "access_token": self.access_token,
    #         "token_type": self.token_type,
    #     }


class TokenData(pydantic.BaseModel):
    username: str | None = None


class User(pydantic.BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(pydantic.BaseModel):
    ID: int
    Name: str
    Surname: str
    Nickname: str
    PasswordHash: int
    CreatedAt: int
    EditedAt: int
