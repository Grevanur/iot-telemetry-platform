import redis
import json

r = redis.Redis(host="localhost", port=6379)


def cache_device_state(device_id, event):

    r.set(
        f"device:{device_id}",
        json.dumps(event)
    )