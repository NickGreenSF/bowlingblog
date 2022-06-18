from flask import Blueprint, g, jsonify, request
from flask_restful import Api, Resource

from bowlingblog.repositories.GameRepository import GameRepository
from bowlingblog.tasks.tasks import save_new_game

game_bp = Blueprint("games", __name__)
game_api = Api(game_bp)


class Games(Resource):
    def get(self):
        gms = GameRepository.get_all()
        return jsonify(games=[gm.to_json() for gm in gms])

    def post(self):
        body = request.get_json()
        score = body.get("score")
        if score is None:
            abort(400, message="Game score not found in request")
        frames = body.get("frames")
        location = body.get("location")
        new_game = save_new_game(score, frames, location)
        return jsonify(new_game.to_json())


game_api.add_resource(Games, "/games")
