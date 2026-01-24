import re


def adress_ip_from_text(text: str) -> list:
    """function that extracts all IPv4 addresses from the text
    """
    pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b'

    return re.findall(pattern, text)


text = """
123.000.003.233, 192.130.0.1, 255.255.255.255, 192.005.0.1, 123.000.003.233
"""

print(adress_ip_from_text(text))
