from abc import ABC
from sqlalchemy.orm import Session, subqueryload
from bowlingblog.db.models import (
    EngineGetter,
    Game,
    User
)


class GameRepository(ABC):
    engine = EngineGetter.get_or_create_engine()

    @classmethod
    def get_all(cls):
        with Session(cls.engine) as session:
            games = session.query(Game).all()
            return games


class UserRepository(ABC):
    engine = EngineGetter.get_or_create_engine()

    @classmethod
    def get_all(cls):
        with Session(cls.engine) as session:
            users = session.query(User).all()
            return users
