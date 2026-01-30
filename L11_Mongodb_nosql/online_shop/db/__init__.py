from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["online_shop"]

products = db["products"]
orders = db["orders"]
