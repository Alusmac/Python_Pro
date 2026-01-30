from utils.date_time import days_ago


def total_sold_products(orders_collection, products_collection, days=30) -> list | None:
    """total sold products
    """
    start_date = days_ago(days)
    pipeline = [
        {"$match": {"created_at": {"$gte": start_date}}},
        {"$unwind": "$items"},
        {"$group": {"_id": "$items.product_id", "total_sold": {"$sum": "$items.quantity"}}}
    ]
    result = list(orders_collection.aggregate(pipeline))
    print(f"\nTotal sold products in the last {days} days:")
    for r in result:
        prod = products_collection.find_one({"_id": r["_id"]})
        print(f"{prod['name']} - {r['total_sold']} units")


def total_spent_by_customer(customer_name: str, orders_collection: int) -> list | None:
    """ total spent by customer
    """
    pipeline = [
        {"$match": {"customer": customer_name}},
        {"$group": {"_id": "$customer", "total_spent": {"$sum": "$total_amount"}}}
    ]
    result = list(orders_collection.aggregate(pipeline))
    if result:
        print(f"\nTotal spent by {customer_name}: {result[0]['total_spent']} USD")
    else:
        print(f"\nNo orders found for {customer_name}")
