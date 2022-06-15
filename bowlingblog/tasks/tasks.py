from bowlingblog.db.models import (EngineGetter, Game)
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from flask_restful import current_app
from sqlalchemy.orm import Session

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)


def save_new_game():
    engine = EngineGetter.get_or_create_engine()
    with Session(engine) as session:
        new_game = Game()
        session.add(new_game)
        assert new_game.id is not None
        session.commit()
        current_app.logger.info("ID: %s", new_game.id)
        return new_game
