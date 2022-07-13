from tkinter.scrolledtext import example

from flask_restx import fields, Model
from jsonschema._validators import required

from project.setup.api.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'description': fields.String(required=True, max_length=100, example='Описание фильма'),
    'trailer': fields.String(required=True),
    'year': fields.Integer(required=True, max_length=5, example=2020),
    'rating': fields.Float(required=True, max_length=5, example=5.5),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, example='name@email.com'),
    'password': fields.String(required=True),
    'name': fields.String(example='Валера'),
    'surname': fields.String(example='Валериевич'),
    'favorite_genre': fields.String(example='боевик'),
})

