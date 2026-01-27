from film_library.dao.movie_dao import MovieDAO
from film_library.dao.actor_dao import ActorDAO
from film_library.dao.movie_cast_dao import MovieCastDAO


class MovieService:
    """Service for movie-related operations
    """

    def __init__(self):
        self.movie_dao = MovieDAO()
        self.actor_dao = ActorDAO()
        self.movie_cast_dao = MovieCastDAO()

    def add_movie(self, title, release_year, genre, actor_names=None):
        """
        Add a movie and link actors by name.
        If actor doesn't exist, create a new one
        """
        title = title.strip().title()
        movie_id = self.movie_dao.add(title, release_year, genre)

        if actor_names:
            for name in actor_names:
                name = name.strip()
                all_actors = self.actor_dao.get_all()
                found = next((a for a in all_actors if a[1].lower() == name.lower()), None)
                if found:
                    actor_id = found[0]
                else:
                    actor_id = self.actor_dao.add(name, None)
                self.movie_cast_dao.add_actor_to_movie(movie_id, actor_id)

        return movie_id

    def get_all_movies(self):
        return self.movie_dao.get_all()

    def get_movie_by_id(self, movie_id):
        return self.movie_dao.get_by_id(movie_id)

    def search_movies(self, keyword):
        return self.movie_dao.search_by_title(keyword)

    def get_paginated_movies(self, limit, offset):
        return self.movie_dao.get_paginated(limit, offset)

    def get_total_count(self):
        return self.movie_dao.count()
