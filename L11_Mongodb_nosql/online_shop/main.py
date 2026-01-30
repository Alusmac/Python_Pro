from db.__init__ import products, orders
from db.orders import add_order
from db.products import add_product_if_not_exists, delete_out_of_stock, create_category_index, get_product_by_name
from redis_cache.sessions import (
    create_session,
    get_session,
    update_last_activity,
    delete_session
)
from summary.reports import total_sold_products, total_spent_by_customer
from utils.date_time import days_ago

products_list = [
    {"name": "Blender", "price": 800, "category": "electronics", "stock": 10},
    {"name": "Toster", "price": 400, "category": "electronics", "stock": 25},
    {"name": "Grill", "price": 1500, "category": "electronics", "stock": 20}
]

for p in products_list:
    add_product_if_not_exists(p)

delete_out_of_stock()
create_category_index()

product1 = get_product_by_name("Blender")
product2 = get_product_by_name("Toster")
product3 = get_product_by_name("Grill")

orders_list = [
    {
        "order_number": "ORD-1001",
        "customer": "Jan Fillmann",
        "items": [{"product_id": product1["_id"], "quantity": 1}],
        "total_amount": product1["price"],
        "created_at": days_ago(4)
    },
    {
        "order_number": "ORD-1002",
        "customer": "Gloria Evimuk",
        "items": [{"product_id": product2["_id"], "quantity": 2}],
        "total_amount": product2["price"] * 2,
        "created_at": days_ago(6)
    },
    {
        "order_number": "ORD-1003",
        "customer": "Emma Klarz",
        "items": [{"product_id": product3["_id"], "quantity": 1}],
        "total_amount": product3["price"],
        "created_at": days_ago(1)
    }
]

for o in orders_list:
    add_order(o)

total_sold_products(orders, products)
total_spent_by_customer("Gloria Evimuk", orders)
total_spent_by_customer("Jan Fillmann", orders)

print("\n****** Redis session demo ******")

session_token = create_session("user_123")
print("Session created:", session_token)

session_data = get_session(session_token)
print("Session data:", session_data)

update_last_activity(session_token)
print("Session updated")

delete_session(session_token)
print("Session deleted")
