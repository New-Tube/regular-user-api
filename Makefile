ARTIFACTS=


ARTIFACTS += src/comment_pb2.py
ARTIFACTS += src/comment_pb2.pyi
ARTIFACTS += src/comment_pb2_grpc.py

ARTIFACTS += src/common_pb2.py
ARTIFACTS += src/common_pb2.pyi
ARTIFACTS += src/common_pb2_grpc.py

ARTIFACTS += src/user_pb2.py
ARTIFACTS += src/user_pb2.pyi
ARTIFACTS += src/user_pb2_grpc.py

ARTIFACTS += src/video_pb2.py
ARTIFACTS += src/video_pb2.pyi
ARTIFACTS += src/video_pb2_grpc.py

ARTIFACTS += src/video_regular_pb2.py
ARTIFACTS += src/video_regular_pb2.pyi
ARTIFACTS += src/video_regular_pb2_grpc.py

ARTIFACTS += src/video_creator_pb2.py
ARTIFACTS += src/video_creator_pb2.pyi
ARTIFACTS += src/video_creator_pb2_grpc.py


.PHONY: generate
generate:
	cd src && \
	python3 -m grpc_tools.protoc -I../internal_api_protos --python_out=. --pyi_out=. --grpc_python_out=. ../internal_api_protos/*.proto

.PHONY: clear
clear:
	rm ${ARTIFACTS}
