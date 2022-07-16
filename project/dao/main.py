from typing import Optional

from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre, Director, Movie, User, movie_favorites


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None):
        stmt: BaseQuery = self._db_session.query(self.__model__)

        if status == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))

        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def __init__(self, db_session) -> None:
        super().__init__(db_session)

    def add_user(self, data_user: dict) -> None:
        user = User(**data_user)
        self._db_session.add(user)
        self._db_session.commit()

    def get_by_email(self, email: str) -> User:
        stmt: BaseQuery = self._db_session.query(self.__model__).filter(self.__model__.email == email)

        if user := stmt.first():
            return user
        else:
            raise ItemNotFound("Нет пользователя с таким email")

    def update(self, user: User) -> None:
        self._db_session.add(user)
        self._db_session.commit()
