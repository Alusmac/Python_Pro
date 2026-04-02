from queue import Queue
from typing import Dict


class OrderService:
    """Produces order-related events into the queue
    """

    def __init__(self, queue: Queue) -> None:
        self.queue = queue

    def create_order(self, order: Dict) -> None:
        """Create an order
        """
        self.queue.put(("order.created", order))

    def pay_order(self, order: Dict) -> None:
        """Pay an order
        """
        self.queue.put(("order.paid", order))
