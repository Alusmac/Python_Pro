import re


def delete_html_hashtags(text: str) -> str:
    """ function that removes all HTML tags from the text.
    """
    pattern = r'<[^>]+>'
    return re.sub(pattern, "", text)


text = """
<!DOCTYPE html>Hello <html>World<head>!
"""

print(delete_html_hashtags(text))
