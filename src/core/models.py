import comment_pb2_grpc
import grpc
import user_pb2
import user_pb2_grpc
import video_creator_pb2_grpc
import video_regular_pb2_grpc

import auth.models
import auth.utils


class StubGenerator:
    def __init__(self, address):
        self._address = address

    def get_channel(self):
        return grpc.insecure_channel(self._address)

    def get_user_stub(self):
        return user_pb2_grpc.UserStub(self.get_channel())

    def get_comment_stub(self):
        return comment_pb2_grpc.CommentStub(self.get_channel())

    def get_video_creator_stub(self):
        return video_creator_pb2_grpc.VideoCreatorUserStub(self.get_channel())

    def get_video_regulat_stub(self):
        return video_regular_pb2_grpc.VideoRegularUserStub(self.get_channel())

    def get_user(self, username=None):
        return self.get_user_stub().Get(
            user_pb2.UserRequest(Nickname=username),
        )

    def create_user(self, user: auth.models.UserRegistrionRequest):
        return self.get_user_stub().Create(
            user_pb2.UserCreateRequest(
                Nickname=user.username,
                PasswordHash=auth.utils.get_password_hash(user.password),
                Name=user.name,
                Surname=user.surname,
            ),
        )
