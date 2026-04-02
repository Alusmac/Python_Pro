from typing import Any


class AnalyticsService:
    """Tracks order statistics.
    """

    def __init__(self) -> None:
        self.orders_created = 0
        self.orders_paid = 0

    def handle_event(self, event_name: str, data: Any) -> None:
        if event_name == "order.created":
            self.orders_created += 1
        elif event_name == "order.paid":
            self.orders_paid += 1

        print(f"ANALYTICS: created={self.orders_created}, paid={self.orders_paid}")
