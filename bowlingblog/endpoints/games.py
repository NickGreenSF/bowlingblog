'''
basic methods for games live here
'''

from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from bowlingblog.repositories.game_repository import GameRepository
from bowlingblog.tasks.tasks import delete_game, save_new_game

game_bp = Blueprint("games", __name__)
game_api = Api(game_bp)


class Games(Resource):
    '''
    basic requests involving games
    '''

    def get(self):
        '''
        gets all games
        '''
        gms = GameRepository.get_all()
        return jsonify(games=[gm.to_json() for gm in gms])

    def post(self):
        '''
        makes new game
        '''
        body = request.get_json()
        score = body.get("score")
        assert score is not None
        frames = body.get("frames")
        assert frames is not None
        location = body.get("location")
        description = body.get("description")
        date = body.get("date")
        uid = body.get("uid")
        assert uid is not None
        splits = body.get("splits")
        new_game = save_new_game(
            score, frames, uid, location, description, date, splits)
        return jsonify(new_game.to_json())

    def delete(self):
        '''
        deletes game by id
        '''
        body = request.get_json()
        gid = body.get("id")
        assert gid is not None
        return delete_game(gid)


game_api.add_resource(Games, "/games")
