"""Module that defines/creates/holds ORMs for the database."""
from datetime import datetime

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
    test = Column(String)


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
