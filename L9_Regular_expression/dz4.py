import re


def date_formatting(event: str) -> str:
    """function that formats dates
    """
    pattern = r'^(\d{2})/(\d{2})/(\d{4})$'
    return re.sub(pattern, r'\3-\2-\1', event)


print(date_formatting("12/08/2000"))
print(date_formatting("01/12/2002"))
