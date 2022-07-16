from flask_restx import Namespace, Resource
from project.setup.api import movie
from project.tools.decoration import authorizations
from project.container import user_movie_service

api = Namespace('favorites')


@api.route('/movies/')
class FavoritesView(Resource):
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    @authorizations
    def get(self, user_id):
        return user_movie_service.get_all_by_uid(user_id)


@api.route('/movies/<int:movie_id>/')
class FavoriteView(Resource):
    @authorizations
    def post(self, movie_id, user_id):
        user_movie_service.add_movie(user_id, movie_id)
        return 200

    @authorizations
    def delete(self, movie_id, user_id):
        user_movie_service.delete_movie(user_id, movie_id)
        return 200
