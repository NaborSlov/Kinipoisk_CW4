from project.dao.main import UserDAO, MovieDAO
from project.exceptions import ItemNotFound
from project.models import User


class UserMovieService:
    def __init__(self, dao_user: UserDAO, dao_movie: MovieDAO):
        self.dao_user = dao_user
        self.dao_movie = dao_movie

    def get_all_by_uid(self, uid: int) -> list[User]:
        items = self.dao_user.get_by_id(uid)
        if items:
            return items.movie_favorites
        else:
            raise ItemNotFound('Нет избранных файлов')

    def add_movie(self, uid: int, mid: int) -> None:
        user = self.dao_user.get_by_id(uid)
        movie = self.dao_movie.get_by_id(mid)
        user.movie_favorites.append(movie)
        self.dao_user.update(user)

    def delete_movie(self, uid: int, mid: int) -> None:
        user = self.dao_user.get_by_id(uid)
        movie = self.dao_movie.get_by_id(mid)
        user.movie_favorites.remove(movie)
        self.dao_user.update(user)
