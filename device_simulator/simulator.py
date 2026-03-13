import asyncio
import json
import random
from datetime import datetime, UTC
from kafka import KafkaProducer

KAFKA_BROKER = "localhost:9092"
TOPIC = "device.telemetry"

NUM_DEVICES = 10000
EVENT_INTERVAL = 5


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def generate_event(device_id):

    return {
        "device_id": f"device_{device_id}",
        "timestamp": datetime.now(UTC).isoformat(),
        "temperature": round(random.uniform(50, 100), 2),
        "battery_level": random.randint(10, 100),
        "signal_strength": random.randint(-90, -40),
    }


async def simulate_device(device_id):

    while True:

        event = generate_event(device_id)

        producer.send(TOPIC, event)

        await asyncio.sleep(EVENT_INTERVAL)


async def main():

    tasks = []

    for device in range(NUM_DEVICES):

        task = asyncio.create_task(simulate_device(device))

        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":

    asyncio.run(main())