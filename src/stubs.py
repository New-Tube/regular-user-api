import comment_pb2_grpc
import user_pb2_grpc
import video_creator_pb2_grpc
import video_regular_pb2_grpc


def stub_user(channel):
    return user_pb2_grpc.UserStub(
        channel,
    )


def stub_comment(channel):
    return comment_pb2_grpc.CommentStub(
        channel,
    )


def stub_video_creator(channel):
    return video_creator_pb2_grpc.VideoCreatorUserStub(
        channel,
    )


def stub_video_regulat(channel):
    return video_regular_pb2_grpc.VideoRegularUserStub(
        channel,
    )
