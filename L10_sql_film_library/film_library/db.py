import sqlite3
from datetime import datetime

DB_PATH = "film_library.db"


def movie_age(release_year: int) -> int:
    """function: returns the age of a movie based on its release year"""
    if release_year is None:
        return None
    return datetime.now().year - release_year


def get_connection():
    """Creates a connection to the database, enables FOREIGN KEY,
    and registers the movie_age() function
    """
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.create_function("movie_age", 1, movie_age)
    return conn


def init_db():
    """Creates all tables if they do not already have been created
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER,
            genre TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movie_cast (
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY(movie_id, actor_id),
            FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE,
            FOREIGN KEY(actor_id) REFERENCES actors(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()
