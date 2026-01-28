from film_library.db import get_connection


class ActorDAO:
    """Class for working with the actors table
    """

    def add(self, name, birth_year):
        """Adding a new actor"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO actors (name, birth_year) VALUES (?, ?);",
            (name, birth_year)
        )

        conn.commit()
        actor_id = cursor.lastrowid
        conn.close()

        return actor_id

    def get_all(self):
        """Getting all actors"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, birth_year FROM actors;")
        actors = cursor.fetchall()

        conn.close()
        return actors

    def get_by_id(self, actor_id):
        """Getting actor by id"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, birth_year FROM actors WHERE id=?;",
            (actor_id,)
        )
        actor = cursor.fetchone()

        conn.close()
        return actor
