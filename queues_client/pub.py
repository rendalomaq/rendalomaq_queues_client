import os
from dataclasses import dataclass, asdict
from typing import Any
import json

import boto3

SQS_MARKS_QUEUE_URL = os.environ.get(
    "SQS_MARKS_QUEUE_URL", 
    "http://localstack:4566/000000000000/marks-queue"
)

sqs = boto3.client(
    "sqs",
    region_name=os.getenv("AWS_REGION" ,"us-east-1"),
    endpoint_url=os.getenv("AWS_SQS_URL", "http://localstack:4566"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY", "test"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS", "test"),
)

@dataclass
class Mark:
    server_time: str
    device_time: str
    longitude: float
    latitude: float
    altitude: float
    protocol: str
    speed: float
    course: float
    address: str
    attributes: dict[str, Any]
    accuracy: float
    network: str


def send_message(queue_url, data: dict[str, Any]) -> str:
    message = json.dumps(data)

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=0,
        MessageBody=message
    )
    return response["MessageId"]


def send_mark(mark: Mark) -> str:
    if not isinstance(mark, Mark):
        raise TypeError("mark must be a Mark")

    return send_message(
        queue_url=SQS_MARKS_QUEUE_URL,
        data=asdict(mark),
    )
