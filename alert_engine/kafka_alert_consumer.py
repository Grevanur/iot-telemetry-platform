from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "device.telemetry",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


def messages():
    for msg in consumer:
        yield msg.value