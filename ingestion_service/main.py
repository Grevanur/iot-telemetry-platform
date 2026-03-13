from kafka_consumer import get_messages
from postgres_db import insert_telemetry_batch

BATCH_SIZE = 500


def run():

    batch = []

    for event in get_messages():

        batch.append(event)

        if len(batch) >= BATCH_SIZE:

            insert_telemetry_batch(batch)

            batch = []


if __name__ == "__main__":
    run()