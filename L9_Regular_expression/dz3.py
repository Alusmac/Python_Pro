import re


def hashtags_return(text: str) -> list:
    """function that returns a list of hashtags from the text
    """
    pattern = r'#([A-Za-z0-9]+)'
    return re.findall(pattern, text)


text = """
#Romeo is a #Montague, and #Juliet a #Capulet. 
Their families are enmeshed in a feud, but the moment they meet—when Romeo
 and his friends attend a party at #Juliet’s house in disguise—the two 
 fall in love and quickly decide that they want to be married.
"""

print(hashtags_return(text))
