from typing import Any


def send_email(event_name: str, data: Any) -> None:
    """Send email when order is created
    """
    if event_name == "order.created":
        print(f"EMAIL: Order created: {data}")


def send_sms(event_name: str, data: Any) -> None:
    """Send SMS when order is paid
    """
    if event_name == "order.paid":
        print(f"SMS: Order paid: {data}")
