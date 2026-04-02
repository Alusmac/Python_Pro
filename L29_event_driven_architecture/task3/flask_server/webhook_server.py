from flask import Flask, request, jsonify
from event_bus import bus
import worker

app = Flask(__name__)


@app.route("/webhook/order", methods=["POST"])
def webhook_order():
    """Receive webhook for order events
    """
    data = request.get_json()
    if not data or "order_id" not in data or "status" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    bus.emit(f"order.{data['status']}", data)

    return jsonify({
        "message": "Event received",
        "event": f"order.{data['status']}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
