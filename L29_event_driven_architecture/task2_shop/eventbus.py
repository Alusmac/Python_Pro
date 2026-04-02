from collections import defaultdict
from typing import Callable, Any


class EventBus:
    """EventBus for dispatching events to subscribers
    """

    def __init__(self) -> None:
        self._subscribers = defaultdict(list)
        self._wildcard_subscribers = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to events
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            self._wildcard_subscribers[prefix].append(callback)
        else:
            self._subscribers[event_name].append(callback)

    def emit(self, event_name: str, data: Any) -> None:
        """Emit an event
        """

        for callback in self._subscribers.get(event_name, []):
            callback(event_name, data)

        for prefix, callbacks in self._wildcard_subscribers.items():
            if event_name.startswith(prefix):
                for callback in callbacks:
                    callback(event_name, data)
