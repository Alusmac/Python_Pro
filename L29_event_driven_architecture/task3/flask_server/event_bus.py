from collections import defaultdict
from typing import Callable, Any, List


class EventBus:
    """Simple EventBus with wildcard support and event log
    """

    def __init__(self) -> None:
        """Initialize the event bus.
        """
        self._subscribers = defaultdict(list)
        self._wildcard_subscribers = defaultdict(list)
        self._event_log = []

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to events
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            self._wildcard_subscribers[prefix].append(callback)
        else:
            self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """Unsubscribe from events
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            if callback in self._wildcard_subscribers[prefix]:
                self._wildcard_subscribers[prefix].remove(callback)
        else:
            if callback in self._subscribers[event_name]:
                self._subscribers[event_name].remove(callback)

    def emit(self, event_name: str, data: Any) -> None:
        """Emit event to all subscribers
        """
        self._event_log.append({"event": event_name, "data": data})

        for callback in self._subscribers.get(event_name, []):
            callback(event_name, data)

        for prefix, callbacks in self._wildcard_subscribers.items():
            if event_name.startswith(prefix):
                for callback in callbacks:
                    callback(event_name, data)

    def get_event_log(self) -> List:
        """Get the event log
        """
        return self._event_log


bus = EventBus()
