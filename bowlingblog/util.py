'''
defines a couple paths we need
'''

from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
DOCKER_POSTGRES_URL = "postgresql://postgres:postgres@db/bowlingblog"


class BowlingException(Exception):
    '''
    Meaningless, meaningless!
    Cried the Teacher.
    Utterly meaningless!
    Everything is meaningless.
    '''
