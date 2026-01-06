class UnknownOperationError(Exception):
    pass


def create_calculator(operator: str):
    """ функція яка приймає оператор (наприклад, '+', '-', '*', '/')

    та повертає функцію для виконання обчислень
    """
    if operator not in {'+', '*', '-', '/'}:
        raise UnknownOperationError("Unknown operator")

    def calculator(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Its must be int or float")

        if operator == "+":
            return a + b

        if operator == "-":
            return a - b

        if operator == "*":
            return a * b

        if operator == "/":
            return a / b

    return calculator


try:
    a = float(input("Please enter a first number: "))
    b = float(input("Please enter a second number: "))
    operator = input("Please enter a operation: (+, -, *, /): ")

    print(f"Your Result: {create_calculator(operator)(a, b)}")

except ZeroDivisionError as e:
    print(f"Error Not possible to divide by zero: {e}")
except ValueError as e:
    print(f"Error wrong number: {e}")
except UnknownOperationError as e:
    print(f"Unknown operator: {e}")
