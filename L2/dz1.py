import builtins


def my_sum() -> None:
    """ функція яка перекриває вбудовану функцію sum

    """
    print("This is my custom sum function!")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(nums))
print(my_sum())
sum = my_sum
print(builtins.sum(nums))
