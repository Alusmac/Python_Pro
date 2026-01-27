import datetime

CURRENT_YEAR = datetime.datetime.now().year

def validate_movie_title(title: str) -> bool:
    """Check that movie title is not empty
    """
    if not title.strip():
        raise ValueError("Movie title cannot be empty.")
    return True

def validate_movie_year(year: int) -> bool:
    """Check that movie release year is reasonable
    """
    if year < 1888 or year > CURRENT_YEAR:
        raise ValueError(f"Movie year must be between 1888 and {CURRENT_YEAR}.")
    return True

def validate_genre(genre: str) -> bool:
    """Check that genre is not empty
    """
    if not genre.strip():
        raise ValueError("Genre cannot be empty.")
    return True

def validate_actor_name(name: str) -> bool:
    """Check that actor name is not empty
    """
    if not name.strip():
        raise ValueError("Actor name cannot be empty.")
    return True

def validate_actor_birth_year(year: int) -> bool:
    """Check that actor birth year is reasonable
    """
    if year is not None and (year < 1800 or year > CURRENT_YEAR):
        raise ValueError(f"Actor birth year must be between 1800 and {CURRENT_YEAR}.")
    return True

def normalize_title_case(text: str) -> str:
    """Convert text to title case
    """
    return text.strip().title()
