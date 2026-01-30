""" Порівняння SQL і NoSQL """

""" PostgreSQL and Mongo Db """
"""1.Виконайте аналогічні CRUD операції для однієї й тієї ж моделі даних.
   2.Проаналізуйте переваги та недоліки кожної системи для різних завдань.
   """
from pymongo import MongoClient
import psycopg2
from datetime import datetime, timedelta, timezone
import json

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# Підключення
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["online_shop"]
mongo_products = mongo_db["products"]
mongo_orders = mongo_db["orders"]

# PostgreSQL
pg_conn = psycopg2.connect(
    dbname="online_shop",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
pg_cur = pg_conn.cursor()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# Створення таблиць SQL
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
pg_cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL,
    category VARCHAR(50),
    stock INT
)
""")

pg_cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_number VARCHAR(20),
    customer VARCHAR(100),
    items JSONB,
    total_amount DECIMAL,
    created_at TIMESTAMP
)
""")
pg_conn.commit()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# CREATE: Продукти
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
products = [
    {"name": "Blender", "price": 800, "category": "electronics", "stock": 10},
    {"name": "Toster", "price": 400, "category": "electronics", "stock": 25},
    {"name": "Grill", "price": 1500, "category": "electronics", "stock": 20}
]

# MongoDB
for p in products:
    if not mongo_products.find_one({"name": p["name"]}):
        mongo_products.insert_one(p)

# PostgreSQL
for p in products:
    pg_cur.execute("SELECT id FROM products WHERE name=%s", (p["name"],))
    if not pg_cur.fetchone():
        pg_cur.execute(
            "INSERT INTO products (name, price, category, stock) VALUES (%s, %s, %s, %s)",
            (p["name"], p["price"], p["category"], p["stock"])
        )
pg_conn.commit()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# CREATE: Замовлення
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
orders = [
    {
        "order_number": "ORD-1001",
        "customer": "Jan Fillmann",
        "items": [{"product": "Blender", "quantity": 1}],
        "total_amount": 800,
        "created_at": datetime.now(timezone.utc) - timedelta(days=4)
    },
    {
        "order_number": "ORD-1002",
        "customer": "Gloria Evimuk",
        "items": [{"product": "Toster", "quantity": 2}],
        "total_amount": 800,
        "created_at": datetime.now(timezone.utc) - timedelta(days=6)
    }
]

# MongoDB
for o in orders:
    if not mongo_orders.find_one({"order_number": o["order_number"]}):
        mongo_orders.insert_one(o)

# PostgreSQL
for o in orders:
    pg_cur.execute("SELECT id FROM orders WHERE order_number=%s", (o["order_number"],))
    if not pg_cur.fetchone():
        pg_cur.execute(
            "INSERT INTO orders (order_number, customer, items, total_amount, created_at) VALUES (%s, %s, %s, %s, %s)",
            (o["order_number"], o["customer"], json.dumps(o["items"]), o["total_amount"], o["created_at"])
        )
pg_conn.commit()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# READ: Продукти і замовлення
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
print("--- MongoDB Products ---")
for p in mongo_products.find({"price": {"$lt": 1000}}):
    print(p)

print("--- PostgreSQL Products ---")
pg_cur.execute("SELECT * FROM products WHERE price < 1000")
for row in pg_cur.fetchall():
    print(row)

print("--- MongoDB Orders ---")
for o in mongo_orders.find({"total_amount": {"$gte": 800}}):
    print(o)

print("--- PostgreSQL Orders ---")
pg_cur.execute("SELECT * FROM orders WHERE total_amount >= 800")
for row in pg_cur.fetchall():
    print(row)

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# UPDATE: Зменшуємо stock
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# MongoDB
mongo_products.update_one({"name": "Blender"}, {"$inc": {"stock": -1}})

# PostgreSQL
pg_cur.execute("UPDATE products SET stock = stock - 1 WHERE name = 'Blender'")
pg_conn.commit()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# DELETE: Видаляємо продукти, яких немає
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# MongoDB
mongo_products.delete_many({"stock": {"$lte": 0}})

# PostgreSQL
pg_cur.execute("DELETE FROM products WHERE stock <= 0")
pg_conn.commit()

# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# Закриття з'єднань
# ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
pg_cur.close()
pg_conn.close()
mongo_client.close()

#┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
# мої висновки:
""" MongoDB набагато зручніший для швидких CRUD І не для дуже офіційної структури 
    PostgreSQL можливо більш зручний для складних структур
При застосуванні дуже сильно залежить де буде використовується які будуть дані який в них буде об'єм

Як на мене Я ознайомилась із тим із тим я звісно зроблю свій вибір MongoDB, бо це набагато гнучкіша база
Більш зрозумілий синтаксис. 
 І набагато менше писати коду))))"""
