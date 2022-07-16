from flask_restx import Namespace, Resource
from project.setup.api import user
from project.container import user_service
from project.setup.api.parsers import pr_passwords, pr_profile
from project.tools.decoration import authorizations

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    @authorizations
    def get(self, user_id):
        return user_service.get_item(user_id)

    @api.expect(pr_profile)
    @authorizations
    def patch(self, user_id):
        user_service.profile_update(user_id, pr_profile.parse_args())
        return 200


@api.route('/password/')
class UserPasswordView(Resource):
    @api.expect(pr_passwords)
    @authorizations
    def put(self, user_id):
        user_service.password_update(user_id, pr_passwords.parse_args())
        return 200


