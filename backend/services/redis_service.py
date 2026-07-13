import json
import redis
from config import Config

redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_DB,
    decode_responses=True,
    socket_timeout=2,
    socket_connect_timeout=2,
)

def get_cache(key):

    data = redis_client.get(key)

    if data:
        return json.loads(data)

    return None


def set_cache(key, value, expiry=300):

    redis_client.setex(
        key,
        expiry,
        json.dumps(value)
    )


def delete_cache(key):
    redis_client.delete(key)