from fastapi import FastAPI

from fastapi.responses import JSONResponse

from src.auth.utils import login_user, create_user, get_token
from src.auth.models import User

app = FastAPI()


@app.post('/register/{username}/{password}/{name}/{surname}')
async def register(username: str, password: str, name: str, surname: str) -> JSONResponse:
    try:
        user = User(username=username, password=password, name=name, surname=surname)
        create_user_request = create_user(username, password, name, surname)
        if create_user_request["status"]:
            access_token = get_token(username)
            response = {"status": "200", "details": "successful registrate", "token": access_token}
        else:
            response = {"status": "400", "details": create_user_request["details"]}
    except ValueError as e:
        response = {"status": "400", "details": e.errors()[0]["msg"]}
    return JSONResponse(content=response)


@app.post('/login/{username}/{password}')
async def login(username: str, password: str) -> JSONResponse:
    try:
        user = User(username=username, password=password)
        login_user_request = login_user(username, password)
        if login_user_request["status"]:
            access_token = get_token(username)
            response = {"status": "200", "details": "successful account login", "token": access_token}
        else:
            response = {"status": "400", "details": login_user_request["details"]}
    except ValueError as e:
        response = {"status": "400", "details": e.errors()[0]["msg"]}
    return JSONResponse(content=response)
