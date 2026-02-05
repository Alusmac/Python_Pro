"""Кешування результатів функції"""


def memoize(func):
    """ функція для зберігання результату в кеш
    """
    result_cache = {}

    def wrapper(a: int) -> int:
        if a in result_cache:
            return result_cache[a]
        result = func(a)
        result_cache[a] = result
        return result

    return wrapper


def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)


factorial = memoize(factorial)

print(factorial(5))
print(factorial(5))


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci = memoize(fibonacci)

print(fibonacci(10))
print(fibonacci(10))
