from fastapi import FastAPI
import grpc

from config import GRPC_ADDRESS     # noqa I202
import stubs as stbs
from user_pb2 import UserRequest
from video_pb2 import VideoRequest
from video_regular_pb2 import VideoStreamRequest


stubs = {}


async def lifespan(app: FastAPI):
    with grpc.insecure_channel(GRPC_ADDRESS) as channel:
        stubs["user"] = stbs.stub_user(channel)
        stubs["comment"] = stbs.stub_comment(channel)
        stubs["video_creator"] = stbs.stub_video_creator(channel)
        stubs["video_regular"] = stbs.stub_video_regulat(channel)
        yield
    pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    try:
        response = stubs["user"].Get(UserRequest(ID=2))
    except Exception as e:
        return {"status": "error", "message": str(e)}
    print("Greeter client received: " + response.Name + " " + response.Status)
    return {"message": GRPC_ADDRESS}


@app.get("/video/{video_id}")
async def video(video_id: int, quality: str):
    try:   # TODO: Quality and User
        response_video_stream = stubs["video_regular"].GetVideoStream(
            VideoStreamRequest(ID=video_id, UserID=1, Quality="qwerty"),
        )
        response_video_info = stubs["video_regular"].GetInfo(
            VideoRequest(ID=video_id, UserID=1),
        )
    except Exception as e:
        return {"status": "error", "message": str(e)}
    print("Greeter client received: " + response_video_info.Status)
    return {
        "video_stream": response_video_stream,
        "video_info": response_video_info,
    }
