from fastapi import APIRouter
import redis
import json

router = APIRouter()

r = redis.Redis(host="redis", port=6379)


@router.get("/devices/{device_id}")
def get_device(device_id: str):

    data = r.get(f"device:{device_id}")

    if data:
        return json.loads(data)

    return {"error": "device not found"}