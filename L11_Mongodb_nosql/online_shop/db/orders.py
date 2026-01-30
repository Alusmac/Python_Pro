from db.__init__ import orders


def add_order(order):
    """add order
    """
    result = orders.insert_one(order)
    print(f"Inserted order {order['order_number']} with ID {result.inserted_id}")
