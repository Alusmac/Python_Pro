import datetime

CURRENT_YEAR = datetime.datetime.now().year


def validate_movie_title(title: str) -> bool:
    """Validate that the movie title is not empty.
    """
    if not title.strip():
        raise ValueError("Movie title cannot be empty.")
    return True


def validate_movie_year(year: int) -> bool:
    """Validate that the movie release year is realistic.
    """
    if year < 1888 or year > CURRENT_YEAR:
        raise ValueError(f"Movie year must be between 1888 and {CURRENT_YEAR}.")
    return True


def validate_genre(genre: str) -> bool:
    """Validate that genre is not empty.
    """
    if not genre.strip():
        raise ValueError("Genre cannot be empty.")
    return True


def validate_actor_name(name: str) -> bool:
    """Validate that actor name is not empty.
    """
    if not name.strip():
        raise ValueError("Actor name cannot be empty.")
    return True


def validate_actor_birth_year(year: int) -> bool:
    """Validate that actor birth year is within a reasonable range.
    """
    if year is not None and (year < 1800 or year > CURRENT_YEAR):
        raise ValueError(f"Actor birth year must be between 1800 and {CURRENT_YEAR}.")
    return True


def normalize_title_case(text: str) -> str:
    """Convert text to title
    Example: 'interstellar' → 'Interstellar'
    """
    return text.strip().title()


def get_int(prompt: str, min_value: int, max_value: int) -> int:
    """Safely request an integer from the user.
    """
    while True:
        value = input(prompt).strip()

        if not value:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            num = int(value)
        except ValueError:
            print("Invalid number. Please enter a valid integer.")
            continue

        if min_value is not None and num < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and num > max_value:
            print(f"Value cannot exceed {max_value}.")
            continue

        return num


def non_empty_string(prompt: str) -> str:
    """Requests a non-empty string from the user.
    Repeats until the input is valid.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: input cannot be empty.")
