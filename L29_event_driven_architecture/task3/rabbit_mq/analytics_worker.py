import pika
import json


def callback(ch, method, properties, body: bytes) -> None:
    """ callback function called when a message is received
    """
    event = json.loads(body)
    print(f"[ANALYTICS] {event}")


connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = connection.channel()

channel.queue_declare(queue="events")

channel.basic_consume(
    queue="events",
    on_message_callback=callback,
    auto_ack=True
)

print("📊 Analytics worker started...")
channel.start_consuming()
