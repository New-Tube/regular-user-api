from fastapi import FastAPI, HTTPException, status

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
            return response
        raise HTTPException(400, detail=create_user_request["details"])
    except Exception as e:
        print(e)
        raise HTTPException(400)


@app.post("/login")
async def login(user: auth.models.UserLoginRequest):
    try:
        user = auth.utils.authenticate_user(user)
        if not user:
            print(not user)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return auth.utils.get_token(user.Nickname)
    except ValueError as e:
        print(e)
        raise HTTPException(400)
