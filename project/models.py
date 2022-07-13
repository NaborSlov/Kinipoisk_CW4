from enum import unique

from sqlalchemy import Column, String, TEXT, INT, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(TEXT(), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(INT(), nullable=False)
    rating = Column(Float(), nullable=False)
    genre_id = Column(INT(), ForeignKey("genres.id"))
    director_id = Column(INT(), ForeignKey("directors.id"))

    genre = relationship("Genre", foreign_keys=genre_id)
    director = relationship("Director", foreign_keys=director_id)


class User(models.Base):
    __tablename__ = "users"

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    name = Column(String(20))
    surname = Column(String(20))
    favorite_genre = Column(String(20))
