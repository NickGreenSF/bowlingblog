'''
root of the python for this repo
look! some gunicorn stuff!
'''

import logging
import os
from pathlib import Path

from bowlingblog.app import app
from bowlingblog.util import ROOT_PATH

gunicorn_logger = logging.getLogger("gunicorn.info")
