from datetime import timedelta

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse

import auth.models
import auth.utils
import core.config


app = FastAPI()


@app.post("/register")
async def register(user: auth.models.UserRegistrionRequest):
    try:
        # TODO: Validation
        create_user_request = auth.utils.create_user(user)
        if create_user_request["status"]:
            access_token = auth.utils.get_token(user.username)
            response = {
                "status": "200",
                "details": "successful registration",
                "token": access_token,
            }
            core.config.stub.create_user(user)
        else:
            response = {
                "status": "400",
                "details": create_user_request["details"],
            }
    except ValueError as e:
        response = {"status": "400", "details": e}
    return response


@app.post("/login")
async def login(user: auth.models.UserLoginRequest):
    try:
        login_user_request = auth.utils.login_user(user)
        if login_user_request["status"]:
            access_token_expires = timedelta(
                minutes=core.config.ACCESS_TOKEN_EXPIRE_MINUTES,
            )
            access_token = auth.utils.create_access_token(
                data={"sub": user.username},
                expires_delta=access_token_expires,
            )
            response = {
                "status": "200",
                "details": "successful account login",
                "token": access_token,
            }
        else:
            response = {
                "status": "400",
                "details": login_user_request["details"],
            }
    except ValueError as e:
        response = {"status": "400", "details": e.errors()[0]["msg"]}
    return JSONResponse(content=response)


@app.post("/token")
async def login_for_access_token(
    form_data: auth.utils.form_data,
) -> auth.models.Token:
    user = auth.utils.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=core.config.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return auth.utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires,
    )
