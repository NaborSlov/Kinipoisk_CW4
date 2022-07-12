from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie
