'''
something that gets the users
'''
from abc import ABC
from sqlalchemy.orm import Session
from bowlingblog.db.models import (
    EngineGetter,
    User
)


class UserRepository(ABC):
    '''
    gets all the users for us
    '''
    engine = EngineGetter.get_or_create_engine()

    @classmethod
    def get_all(cls):
        '''
        look the method!
        '''
        with Session(cls.engine) as session:
            users = session.query(User).all()
            return users
