from film_library.db import get_connection


class MovieDAO:
    """Class for working with the movies table
    """

    def add(self, title, release_year, genre):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?);",
            (title, release_year, genre)
        )

        conn.commit()
        movie_id = cursor.lastrowid
        conn.close()

        return movie_id

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, release_year, genre FROM movies;")
        movies = cursor.fetchall()

        conn.close()
        return movies

    def get_by_id(self, movie_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, title, release_year, genre FROM movies WHERE id=?;",
            (movie_id,)
        )
        movie = cursor.fetchone()

        conn.close()
        return movie

    def search_by_title(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, title, release_year, genre FROM movies WHERE title LIKE ?;",
            (f"%{keyword}%",)
        )
        movies = cursor.fetchall()

        conn.close()
        return movies

    def get_paginated(self, limit, offset):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, title, release_year, genre FROM movies LIMIT ? OFFSET ?;",
            (limit, offset)
        )
        movies = cursor.fetchall()

        conn.close()
        return movies

    def count(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM movies;")
        count = cursor.fetchone()[0]

        conn.close()
        return count
