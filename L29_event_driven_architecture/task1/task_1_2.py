from collections import defaultdict
from typing import Callable, List, Any


class EventBus:
    """simple EventBus implementation
    """

    def __init__(self) -> None:
        self._subscribers = defaultdict(list)
        self._wildcard_subscribers = defaultdict(list)
        self._event_log = []

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe a callback to an event
        """
        if "*" in event_name:
            prefix: str = event_name.split("*")[0]
            self._wildcard_subscribers[prefix].append(callback)
        else:
            self._subscribers[event_name].append(callback)

    def emit(self, event_name: str, data: Any) -> None:
        """Emit an event and notify all relevant subscribers.
        """
        self._event_log.append({
            "event": event_name,
            "data": data
        })

        for callback in self._subscribers.get(event_name, []):
            callback(event_name, data)

        for prefix, callbacks in self._wildcard_subscribers.items():
            if event_name.startswith(prefix):
                for callback in callbacks:
                    callback(event_name, data)

    def get_event_log(self) -> List:
        """Retrieve the event log.
        """
        return self._event_log


def email_sender(event_name: str, data: Any) -> None:
    """Sends email notifications for user-related events.
    """
    print(f"EMAIL: {event_name}: {data}")


def logger(event_name: str, data: Any) -> None:
    """Logs all events.
    """
    print(f"LOGGER: {event_name} -> {data}")


def analytics(event_name: str, data: Any) -> None:
    """Sends event data to analytics system.
    """
    print(f"ANALYTICS: {event_name}: {data}")


if __name__ == "__main__":
    event: EventBus = EventBus()

    event.subscribe("user.registered", email_sender)
    event.subscribe("*", logger)
    event.subscribe("user.*", analytics)
    event.subscribe("order.created", analytics)

    event.emit("user.registered", {"email": "avp@gmail.com"})
    event.emit("user.deleted", {"user_id": 35})
    event.emit("order.created", {"order_id": 1001, "amount": 250})
