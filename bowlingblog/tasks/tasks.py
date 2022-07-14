'''
this is where most of the actual talking to the db takes place
'''
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from flask_restful import current_app
from sqlalchemy.orm import Session
from bowlingblog.db.models import (EngineGetter, Game, User)

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)


def save_new_game(score, frames, uid, location=None, description=None, date=None):
    '''
    takes in game info and saves the game using those fields
    '''
    user = get_user_by_uid(uid)
    assert user is not None
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        new_game = Game(score=score, frames=frames,
                        location=location, description=description, date=date,
                        firebase_id=uid, username=user.username)
        session.add(new_game)
        assert new_game.score is not None
        assert new_game.frames is not None
        session.commit()
        current_app.logger.info("Score: %s", new_game.score)
        return new_game


def save_new_user(username, firebase_id):
    '''
    makes new user, all we store is firebase id and username, firebase stores passwords
    '''
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        session.expire_on_commit = False
        new_user = User(firebase_id=firebase_id, username=username)
        session.add(new_user)
        session.commit()
        return new_user


def get_user_by_uid(uid):
    '''
    pulls out a user based on firebase id
    '''
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        user = session.query(User).filter(
            User.firebase_id == uid).one_or_none()
        return user


def get_user_games(uid):
    '''
    gets user id, then gets all games with that id
    '''
    user = get_user_by_uid(uid)
    assert user is not None
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        games = session.query(Game).filter(
            Game.firebase_id == user.firebase_id)
        return games


def delete_game(game_id):
    '''
    gets game and deletes it
    '''
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        game = (session.query(Game).filter(
            Game.id == game_id)).one_or_none()
        assert game is not None
        session.delete(game)
        session.commit()
        return True
