from db.__init__ import products


def add_product_if_not_exists(product) -> None:
    """ add product if it doesn't exist
    """
    existing = products.find_one({"name": product["name"]})
    if not existing:
        result = products.insert_one(product)
        print(f"Added product: {product['name']} (ID: {result.inserted_id})")
    else:
        print(f"Product already exists: {product['name']}")


def delete_out_of_stock() -> None:
    """delete out of stock products
    """
    result = products.delete_many({"stock": {"$lte": 0}})
    print(f"Deleted {result.deleted_count} products out of stock")


def create_category_index() -> None:
    """create category index ASCENDING
    """
    products.create_index([("category", 1)])
    print("Index created on 'category'")


def get_product_by_name(name: str) -> dict:
    """get product by name
    """
    return products.find_one({"name": name})
