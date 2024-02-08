from datetime import datetime, timedelta

from Crypto.Hash import BLAKE2s
from fastapi import HTTPException, status
from jose import jwt, JWTError

from auth import models
from core.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY,
    stub,
)


def login_user(user: models.UserLoginRequest) -> dict:
    return {"status": True, "details": ""}


def create_user(user: models.UserRegistrionRequest) -> dict:
    return {"status": True, "details": ""}


def create_access_token(
        data: dict, expires_delta: timedelta | None = None,
) -> jwt:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return models.Token(
        access_token=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM),
        token_type="bearer",
    )


def get_token(username: str) -> jwt:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token(
        data={"sub": username}, expires_delta=access_token_expires,
    )


def verify_password(plain_password, hashed_password):
    return get_password_hash(plain_password) == hashed_password


def get_password_hash(password):
    return int.from_bytes(
        BLAKE2s.new(
            data=password.encode("ascii"),
            digest_bits=32).digest(),
        "big",
    )


def get_user(username: str) -> models.UserInDB:
    if user := stub.get_user(username=username):
        return models.UserInDB(
            ID=user.ID,
            Nickname=user.Nickname,
            Name=user.Name,
            Surname=user.Surname,
            PasswordHash=user.PasswordHash,
            EditedAt=user.EditedAt,
            CreatedAt=user.CreatedAt,
        )

    return None


def authenticate_user(request: models.UserLoginRequest):
    user = get_user(request.username)
    if not user:
        return False
    if not verify_password(request.password, user.PasswordHash):
        return False
    return user


async def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = models.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
