import json
import os
from typing import Any

import boto3

from .entities import Event, serialize_event

SQS_GPS_EVENT_QUEUE_URL = os.environ.get(
    "SQS_GPS_EVENT_QUEUE_URL", "http://localstack:4566/000000000000/marks-queue"  # noqa
)

sqs = boto3.client(
    "sqs",
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    endpoint_url=os.getenv("AWS_SQS_URL", "http://localstack:4566"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY", "test"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS", "test"),
)


def send_message(queue_url, data: dict[str, Any]) -> str:
    message = json.dumps(data)

    response = sqs.send_message(QueueUrl=queue_url, DelaySeconds=0, MessageBody=message)
    return response["MessageId"]


def send_event(event: Event) -> str:
    if not isinstance(event, Event):
        raise TypeError("event must be a Event instance")

    return send_message(
        queue_url=SQS_GPS_EVENT_QUEUE_URL,
        data=serialize_event(event),
    )
