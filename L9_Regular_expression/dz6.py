import re


def valid_password(password: str) -> bool:
    """function that checks whether a password is strong
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!^*?_+-])[A-Za-z\d@#$%&!^*?_+-]{8,}$'
    return bool(re.match(pattern, password))


print(valid_password('Aaaaa88@s3'))
print(valid_password('Abgj34A'))
print(valid_password('Aaaaa88s3'))
print(valid_password('hjgh3Gkh'))
