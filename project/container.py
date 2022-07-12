from project.dao import GenresDAO, DirectorDAO

from project.services import GenresService, DirectorsService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
