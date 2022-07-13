from flask_restx import Namespace, Resource
from project.setup.api import parser, user
from project.container import user_service

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @api.expect(parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        pass
        # """
        # Get all users.
        # """
        # return user_service.get_all(**parser.parse_args())
