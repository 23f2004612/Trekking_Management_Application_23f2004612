import json
import redis
from config import Config

redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_DB,
    decode_responses=True,
    socket_connect_timeout=0.2,
    socket_timeout=0.2,
)

try:
    redis_client.ping()
    REDIS_AVAILABLE = True
    print("Redis Connected")
except Exception:
    REDIS_AVAILABLE = False
    print("Redis Unavailable - Cache Disabled")


def get_cache(key):

    if not REDIS_AVAILABLE:
        return None

    try:
        data = redis_client.get(key)

        if data:
            return json.loads(data)

    except Exception:
        return None

    return None


def set_cache(key, value, expiry=300):

    if not REDIS_AVAILABLE:
        return

    try:
        redis_client.setex(
            key,
            expiry,
            json.dumps(value)
        )

    except Exception:
        pass


def delete_cache(key):

    if not REDIS_AVAILABLE:
        return

    try:
        redis_client.delete(key)

    except Exception:
        pass