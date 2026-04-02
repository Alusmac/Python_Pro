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
        """subscribe event
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            self._wildcard_subscribers[prefix].append(callback)
        else:
            self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """unsubscribe event
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            if callback in self._wildcard_subscribers[prefix]:
                self._wildcard_subscribers[prefix].remove(callback)
        else:
            if callback in self._subscribers[event_name]:
                self._subscribers[event_name].remove(callback)

    def emit(self, event_name: str, data: Any) -> None:
        """ emit an event and notify all relevant subscribers
        """
        self._event_log.append({
            "event": event_name,
            "data": data
        })

        for callback in self._subscribers.get(event_name, []):
            callback(data)

        for prefix, callbacks in self._wildcard_subscribers.items():
            if event_name.startswith(prefix):
                for callback in callbacks:
                    callback(event_name, data)


    def get_event_log(self) -> List:
        """ get event log
        """
        return self._event_log


def send_welcome_email(data) -> None:
    """ send welcome email
    """
    print(f"EMAIL: Send to {data['email']}")


def log_all_user_events(event_name, data) -> None:
    """ log all user events
    """
    print(f"LOG: {event_name}: {data}")


event = EventBus()

event.subscribe("user.registered", send_welcome_email)
event.subscribe("user.*", log_all_user_events)

event.emit("user.registered", {"email": "avp@gmail.com"})

