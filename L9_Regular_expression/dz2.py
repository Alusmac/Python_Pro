import re


def find_phone_numbers_from_text(text: str) -> list:
    """function that finds all phone numbers in the text
    """
    pattern = r'\(?\d{3}\)?[.\-\s]?\d{3}[.\-\s]?\d{4}'
    return re.findall(pattern, text)


text = """
If you feels not good you can call me:(123) 456-7890
If somthing else: 123-456-7890
If you want to know the weather: 123.456.7890
Else: 1234567890

"""

print(find_phone_numbers_from_text(text))
