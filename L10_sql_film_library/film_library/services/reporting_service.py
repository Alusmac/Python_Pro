from film_library.db import get_connection


class ReportingService:
    """class that makes requests:
    JOIN,
    DISTINCT,
    COUNT,
    AVG,
    LIKE,
    UNION,
    LIMIT/OFFSET
    """

    def __init__(self):
        pass

    def movies_with_actors(self):
        """List of films with actors
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT m.title, GROUP_CONCAT(a.name, ', ') AS actors
            FROM movies m
            LEFT JOIN movie_cast mc ON m.id = mc.movie_id
            LEFT JOIN actors a ON mc.actor_id = a.id
            GROUP BY m.id, m.title;
        """)

        result = cursor.fetchall()
        conn.close()
        return result

    def unique_genres(self):
        """Unique genres
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT genre FROM movies;")
        result = [row[0] for row in cursor.fetchall()]
        conn.close()
        return result

    def count_movies_by_genre(self):
        """Number of films by genre
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT genre, COUNT(*) 
            FROM movies
            GROUP BY genre;
        """)
        result = cursor.fetchall()
        conn.close()
        return result

    def avg_actor_birth_by_genre(self, genre):
        """Average birth year of actors in movies of a given genre
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT AVG(a.birth_year)
            FROM actors a
            INNER JOIN movie_cast mc ON a.id = mc.actor_id
            INNER JOIN movies m ON mc.movie_id = m.id
            WHERE m.genre = ? COLLATE NOCASE;
        """, (genre,))
        avg_year = cursor.fetchone()[0]
        conn.close()
        return avg_year

    def search_movies_like(self, keyword):
        """Search for movies by keyword (LIKE)"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, release_year, genre FROM movies WHERE title LIKE ?;", (f"%{keyword}%",))
        result = cursor.fetchall()
        conn.close()
        return result

    def all_actors_and_movies_union(self):
        """Names of all actors and titles of all films (UNION)
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name FROM actors
            UNION
            SELECT title FROM movies;
        """)
        result = [row[0] for row in cursor.fetchall()]
        conn.close()
        return result

    def movies_with_age(self):
        """List of films with their age
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title, movie_age(release_year) FROM movies;")
        result = cursor.fetchall()
        conn.close()
        return result
