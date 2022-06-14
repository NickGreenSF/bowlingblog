import dramatiq
from dramatiq.brokers.redis import RedisBroker
from flask_restful import current_app

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)


def ex():
    return ["hello"]
