import datetime
from dataclasses import asdict, dataclass
from typing import Any


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


def serialize_event(event: Event) -> dict[str, Any]:
    data = asdict(event)
    data["type"] = event.__class__.__name__.lower()
    data["server_time"] = datetime.datetime.now().isoformat()
    return data


if __name__ == "__main__":
    from pprint import pprint

    pos = Position(
        raw_message="",
        device_id="",
        device_time="",
        longitude=0.0,
        latitude=0.0,
        altitude=0.0,
    )
    pprint(serialize_event(pos))
