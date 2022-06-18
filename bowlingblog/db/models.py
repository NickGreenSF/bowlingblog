"""Module that defines/creates/holds ORMs for the database."""
from datetime import datetime
from email.policy import default

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import declarative_base, relationship, backref

from bowlingblog.util import DOCKER_POSTGRES_URL, BowlingException

Base = declarative_base()


class NotFoundException(BowlingException):
    pass


class Game(Base):
    """game table"""

    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    frames = Column(String(63))  # nullable
    location = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="games")

    def __repr__(self):
        return f"Game(id={self.id})"

    def to_json(self):
        return {"id": self.id, "score": self.score, "frames": self.frames, "location": self.location, "user_id": self.user_id}


class User(Base):
    """User table."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    firebase_id = Column(String(255), nullable=False, unique=True)
    admin = Column(Boolean, default=False)
    has_input_frames = Column(Boolean, default=False)
    games = relationship("Game", back_populates="user")
    total_score = Column(Integer)
    total_games = Column(Integer)
    total_strikes = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    def to_json(self):
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
    engine = EngineGetter.get_or_create_engine()
    Base.metadata.drop_all(engine)
