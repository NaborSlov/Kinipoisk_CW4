from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        return self.dao.get_all(page=page)
