from film_library.db import get_connection


class MovieCastDAO:
    """Class for working between movies and actors
    """

    def add_actor_to_movie(self, movie_id, actor_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR IGNORE INTO movie_cast (movie_id, actor_id) VALUES (?, ?);",
            (movie_id, actor_id)
        )

        conn.commit()
        conn.close()

    def get_actors_for_movie(self, movie_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT actors.id, actors.name, actors.birth_year
            FROM actors
            INNER JOIN movie_cast ON actors.id = movie_cast.actor_id
            WHERE movie_cast.movie_id = ?;
        """, (movie_id,))

        actors = cursor.fetchall()
        conn.close()
        return actors

    def get_movies_for_actor(self, actor_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT movies.id, movies.title, movies.release_year, movies.genre
            FROM movies
            INNER JOIN movie_cast ON movies.id = movie_cast.movie_id
            WHERE movie_cast.actor_id = ?;
        """, (actor_id,))

        movies = cursor.fetchall()
        conn.close()
        return movies
