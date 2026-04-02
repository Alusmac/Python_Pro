import threading
import time
from queue import Queue, Empty
from eventbus import EventBus
from order import OrderService
from notification import send_email, send_sms
from analytics import AnalyticsService


def worker(queue: Queue, bus: EventBus) -> None:
    """Worker that consumes events from queue and processes them
    """
    while True:
        try:
            event_name, data = queue.get(timeout=1)
            bus.emit(event_name, data)
        except Empty:
            continue
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    queue: Queue = Queue()
    bus = EventBus()

    order_service = OrderService(queue)
    analytics = AnalyticsService()

    bus.subscribe("order.created", send_email)
    bus.subscribe("order.paid", send_sms)
    bus.subscribe("order.*", analytics.handle_event)

    t = threading.Thread(target=worker, args=(queue, bus), daemon=True)
    t.start()

    order_service.create_order({"id": 1, "amount": 250})
    order_service.pay_order({"id": 1, "amount": 250})

    order_service.create_order({"id": 2, "amount": 450})

    time.sleep(2)
