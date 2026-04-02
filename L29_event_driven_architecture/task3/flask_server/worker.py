from typing import Any
from event_bus import bus


def email_worker(event_name: str, data: Any) -> None:
    """email worker function
    """
    print(f"[EMAIL WORKER] Send email for {event_name}: {data}")


def log_worker(event_name: str, data: Any) -> None:
    """log worker function
    """
    print(f"[LOG WORKER] Event {event_name} received with data: {data}")


bus.subscribe("order.created", email_worker)
bus.subscribe("order.*", log_worker)
