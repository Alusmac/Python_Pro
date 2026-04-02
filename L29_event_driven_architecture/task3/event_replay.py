import json
from collections import defaultdict
from typing import Callable, Any


class EventBus:
    """EventBus with logging and replay support
    """

    def __init__(self, log_file: str = "events.log") -> None:
        self._subscribers = defaultdict(list)
        self._wildcard_subscribers = defaultdict(list)
        self._log_file = log_file

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to events
        """
        if "*" in event_name:
            prefix = event_name.split("*")[0]
            self._wildcard_subscribers[prefix].append(callback)
        else:
            self._subscribers[event_name].append(callback)

    def emit(self, event_name: str, data: Any) -> None:
        """Emit data to events in JSON format
        """

        with open(self._log_file, "a") as f:
            f.write(json.dumps({
                "event": event_name,
                "data": data
            }) + "\n")

        self._dispatch(event_name, data)

    def _dispatch(self, event_name: str, data: Any) -> None:
        """Dispatch data to events
        """
        for callback in self._subscribers.get(event_name, []):
            callback(event_name, data)

        for prefix, callbacks in self._wildcard_subscribers.items():
            if event_name.startswith(prefix):
                for callback in callbacks:
                    callback(event_name, data)

    def replay_from_file(self, file_path: str) -> None:
        """Replay events from a log file
        """
        print("\n Replaying events...\n")

        with open(file_path, "r") as f:
            for line in f:
                record = json.loads(line.strip())
                self._dispatch(record["event"], record["data"])


def logger(event_name, data) -> None:
    """Log events
    """
    print(f"LOG: {event_name}: {data}")


event = EventBus()

event.subscribe("*", logger)

event.emit("order.created", {"id": 1})
event.emit("order.paid", {"id": 1})

event.replay_from_file("events.log")
