'''
the main python file. sets up the app container, referred to in the logs as bowlingblog
'''


import logging
from os.path import dirname

from flask import Flask, jsonify
from flask_cors import CORS

# App Blueprints: Blueprint for each resource
from bowlingblog.endpoints.games import game_bp
from bowlingblog.endpoints.users import user_bp

API_PREFIX_V1 = "/api/v1"


# def register_blueprints(app):
#     """Register all blueprints for the app."""
#     app.register_blueprint(game_bp, url_prefix=API_PREFIX_V1)
#     app.register_blueprint(user_bp, url_prefix=API_PREFIX_V1)
#     pass


app = Flask(__name__)
path = dirname(__file__)
CORS(app)
# register_blueprints(app)
app.register_blueprint(game_bp, url_prefix=API_PREFIX_V1)
app.register_blueprint(user_bp, url_prefix=API_PREFIX_V1)
if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route("/api/hello/", methods=["GET"])
def hello():
    '''
    testing if you have the api working
    '''
    return jsonify(success=True)


@app.errorhandler(404)
def route_not_found():
    '''
    standard 404 we don't have that error
    '''
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
