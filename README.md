# Usage

## Installation

`pip install git+https://github.com/rendalomaq/rendalomaq_queues_client#1`

## Environment variables required

- SQS_GPS_EVENT_QUEUE_URL
- AWS_REGION
- AWS_SQS_URL
- AWS_ACCESS_KEY
- AWS_SECRET_ACCESS

```python
from queues_client.entities import Position
from queues_client.pub import send_event

message_id = send_event(
    Position(...)
)
```

## Payloads

```python
@dataclass
class Event:
    raw_message: str
    device_id: str


@dataclass
class Position(Event):
    device_time: str
    longitude: float
    latitude: float
    altitude: float
    satellites_count: int = 0
    speed: float = 0.0
    mcc: int = 0
    mnc: int = 0
    lac: str = ""
    cell_id: str = ""
```
