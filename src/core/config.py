import os

from dotenv import load_dotenv

import core.models

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"),
)
GRPC_ADDRESS = os.environ.get("GRPC_ADDRESS")

stub = core.models.StubGenerator(GRPC_ADDRESS)
