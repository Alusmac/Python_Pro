from film_library.dao.actor_dao import ActorDAO
from film_library.dao.movie_cast_dao import MovieCastDAO


class ActorService:
    """clas which working will all services included actors
    """
    def __init__(self):
        self.actor_dao = ActorDAO()
        self.movie_cast_dao = MovieCastDAO()

    def add_actor(self, name, birth_year):
        """Adding actor"""
        return self.actor_dao.add(name, birth_year)

    def get_all_actors(self):
        """Getting all actors"""
        return self.actor_dao.get_all()

    def get_actor_by_id(self, actor_id):
        """Getting actor by id"""
        return self.actor_dao.get_by_id(actor_id)

    def get_movies_for_actor(self, actor_id):
        """Getting movies from actor"""
        return self.movie_cast_dao.get_movies_for_actor(actor_id)
