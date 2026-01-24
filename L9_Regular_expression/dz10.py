import re


def search_words(text: str) -> list:
    """searches words in the text from poem
    """
    pattern = r'\b(Romeo|Juliet|Montague|Capulet)\b'
    return re.findall(pattern, text)


text = """
The prologue of Romeo and Juliet calls the title characters “star-crossed lovers”—and 
the stars do seem to conspire against these young lovers.
Romeo is a Montague, and Juliet a Capulet. Their families are enmeshed 
in a feud, but the moment they meet—when Romeo and his friends attend a party at 
Juliet house in disguise—the two fall in love and quickly decide that they want to be married.
"""

print(search_words(text))
