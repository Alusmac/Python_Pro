import uuid


def uuid_generator():
    """ ітератор, який генерує унікальні ідентифікатори.
    """
    while True:
        yield str(uuid.uuid4())


gen = uuid_generator()

for _ in range(7):
    print(next(gen))
