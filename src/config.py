import os

from dotenv import load_dotenv

load_dotenv()

GRPC_ADDRESS = os.environ.get(
    "GRPC_ADDRESS",
    "internal-api.dev.new-tube.ru:4000",
)
