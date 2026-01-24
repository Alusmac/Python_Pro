import re


def delete_url_from_text(text: str) -> str:
    """function that deletes all URLs from the specified text.
    """
    pattern = r'(https?://[^\s]+)'
    return re.sub(pattern, '', text)


text = """
"To be, or not to be, that is the question" is the opening line of a 
famous soliloquy from William Shakespeare's Hamlet (Act III, Scene I), spoken by Prince Hamlet.
https://www.folger.edu/explore/shakespeares-works/romeo-and-juliet/read/
https://shakespeare.mit.edu/hamlet/index.html
Context: Spoken in the Wikipedia nunnery scene, this soliloquy occurs as Hamlet waits for
 Ophelia, reflecting his deep despair and philosophical questioning of life. 
https://www.backstage.com/magazine/article/underused-shakespeare-monologues-72090/
"""

print(delete_url_from_text(text))
