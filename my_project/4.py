#Зробити калькулятор (+, -, *, /) для двох чисел.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("+,-,*,/: ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else: print("Invalid input")

