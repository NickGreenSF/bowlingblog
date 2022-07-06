'''
something that gets the games
'''
from abc import ABC
from sqlalchemy.orm import Session
from bowlingblog.db.models import (
    EngineGetter,
    Game
)


class GameRepository(ABC):
    '''
    gets the games for us
    '''
    engine = EngineGetter.get_or_create_engine()

    @classmethod
    def get_all(cls):
        '''
        look the method!
        '''
        with Session(cls.engine) as session:
            games = session.query(Game).all()
            return games
