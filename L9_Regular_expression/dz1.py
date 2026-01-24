import re


def correct_email(email: str) -> bool:
    """function that checks whether an email address is correct
    """
    pattern = r'^[A-Za-z0-9](?:[A-Za-z0-9\.]*[A-Za-z0-9])?@[A-Za-z0-9]+\.[A-Za-z]{2,6}$'
    return bool(re.match(pattern, email))


print(correct_email("neo24@gmail.com"))
print(correct_email(".neo24@gmail.com"))
print(correct_email("neo.@dgmail.com"))
print(correct_email("neo@gmail.c"))
