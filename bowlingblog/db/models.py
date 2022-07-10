"""Module that defines/creates/holds ORMs for the database."""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship

from bowlingblog.util import DOCKER_POSTGRES_URL, BowlingException

Base = declarative_base()


class NotFoundException(BowlingException):
    '''
    this doesn't do anything
    '''


class Game(Base):
    """game table"""

    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    # not nullable. Whether this is or isn't nullable changes the function of the app.
    frames = Column(String(63), nullable=False)
    location = Column(String(255))
    firebase_id = Column(String(255), ForeignKey("users.firebase_id"))
    username = Column(String(255))
    description = Column(String(2000))
    date = Column(String(255))

    def __repr__(self):
        return f"Game(id={self.id})"

    def to_json(self):
        '''
        how this object is returned to the front end
        '''
        return {"id": self.id, "score": self.score, "frames": self.frames,
                "location": self.location, "user_id": self.firebase_id,
                "username": self.username, "description": self.description}


class User(Base):
    """User table."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    firebase_id = Column(String(255), nullable=False, unique=True)
    admin = Column(Boolean, default=False)
    total_score = Column(Integer)
    total_games = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    def to_json(self):
        '''
        how this object is returned to the front end
        '''
        return {"username": self.username, "firebase_id": self.firebase_id}


class EngineGetter:
    """Thing to get the engine."""

    _engine = None

    @classmethod
    def get_or_create_engine(cls):
        """Get a sql connection engine or return the extant one."""
        if cls._engine is None:
            cls._engine = create_engine(
                DOCKER_POSTGRES_URL, echo=True, future=True)
        return cls._engine


def clear_models():
    '''
    delete everything lol
    '''
    engine = EngineGetter.get_or_create_engine()
    Base.metadata.drop_all(engine)
