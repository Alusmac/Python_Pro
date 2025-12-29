def create_calculator(operator: str):
    """ функція яка приймає оператор (наприклад, '+', '-', '*', '/')

    та повертає функцію для виконання обчислень
    """

    def calculator(num1, num2):
        if operator == "+":
            return num1 + num2

        if operator == "-":
            return num1 - num2

        if operator == "*":
            return num1 * num2

        if operator == "/":
            if num2 == 0:
                return "Помилка ділення на 0!"
        return num1 / num2

    return calculator


add = create_calculator('+')
sub = create_calculator('-')
mul = create_calculator('*')
div = create_calculator('/')

print(add(0.5, 5))
print(sub(25, 5))
print(mul(5, 5))
print(div(35, 5))
print(div(11, 0))
