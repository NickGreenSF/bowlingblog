from flask import Blueprint, g, jsonify, request
from flask_restful import Api, Resource

from bowlingblog.repositories.UserRepository import UserRepository
from bowlingblog.tasks.tasks import save_new_user, get_user_games

user_bp = Blueprint("users", __name__)
user_api = Api(user_bp)


class Users(Resource):
    def get(self):
        gms = UserRepository.get_all()
        return jsonify(users=[gm.to_json() for gm in gms])

    def post(self):
        body = request.get_json()
        username = body.get("username")
        firebase_id = body.get("firebase_id")
        new_user = save_new_user(username, firebase_id)
        return jsonify(new_user.to_json())


class UserGames(Resource):
    def get(self, user_id):
        gms = get_user_games(user_id)
        return jsonify(games=[gm.to_json() for gm in gms])


user_api.add_resource(Users, "/users")
user_api.add_resource(UserGames, "/users/<string:user_id>")
