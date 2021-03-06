import abc
from typing import List

from domainmodel.model import Movie, Genre, User, Review, Actor, WatchList, Director

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor: Actor) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self) -> List[Genre]:
        """ Returns the Genres stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        if review.movie is None:
            raise RepositoryException('Comment not correctly attached to a User')

    @abc.abstractmethod
    def get_review(self):
        """ Returns the reviews stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """ Adds a Genre to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director: str) -> Director:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie: str) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ids_for_genre(self, genre_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_list_by_id_list(self, id_list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_name(self, title: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director_list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self):
        raise NotImplementedError
