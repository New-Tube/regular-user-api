from pydantic import BaseModel, constr, field_validator


class User(BaseModel):
    name: str = ""
    surname: str = ""
    username: str
    password: constr(min_length=8, max_length=16)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str):
        username_length = len(value)
        if username_length < 1 or username_length > 16:
            raise ValueError("The username must be between 1 and 16 characters long")
        return value

    @field_validator("password")
    @classmethod
    def validate_email(cls, value: str) -> str:
        password_length = len(value)
        if password_length < 8 or password_length > 16:
            raise ValueError("The password must be between 8 and 16 characters long")
        return value
