import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = connection.channel()

channel.queue_declare(queue="events")

event = {
    "event": "user.registered",
    "data": {"email": "avp@gmail.com"}
}

channel.basic_publish(
    exchange="",
    routing_key="events",
    body=json.dumps(event)
)

print("✅ Event sent")

connection.close()
