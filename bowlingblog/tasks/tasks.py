from bowlingblog.db.models import (EngineGetter, Game, User)
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from flask_restful import current_app
from sqlalchemy.orm import Session

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)

# engine = EngineGetter.get_or_create_engine()
# with Session(engine) as session:
#     session.expire_on_commit = False
#     new_user = User(firebase_id="test", username="N")
#     session.add(new_user)
#     session.commit()

# frames_1 = "9-|7/|9/|62|X|9/|X|7/|63|X9-"
# frames_2 = "9/|71|X|9/|72|7/|X|7/|X|9/8"
# frames_3 = "X|X|72|9/|7/|9-|X|9-|X|72-"
# scores = [156, 169, 156]

# engine = EngineGetter.get_or_create_engine()
# with Session(engine) as session:
#     new_game = Game(score=scores[2], frames=frames_3,
#                     location="Earl Anthony's Dublin Bowl", user_id=1)
#     session.add(new_game)
#     assert new_game.score is not None
#     session.commit()
#     current_app.logger.info("Score: %s", new_game.score)


def save_new_game(score, frames, location=None):
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        new_game = Game(score=score, frames=frames,
                        location=location, user_id=1)
        session.add(new_game)
        assert new_game.score is not None
        assert new_game.frames is not None
        session.commit()
        current_app.logger.info("Score: %s", new_game.score)
        return new_game


def save_new_user(username, firebase_id):
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        session.expire_on_commit = False
        new_user = User(firebase_id=firebase_id, username=username)
        session.add(new_user)
        session.commit()
        return new_user
