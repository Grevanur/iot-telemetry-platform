import psycopg2
from psycopg2.extras import execute_batch

conn = psycopg2.connect(
    host="localhost",
    database="telemetry",
    user="admin",
    password="admin"
)


def insert_telemetry_batch(events):

    query = """
    INSERT INTO telemetry
    (device_id, timestamp, temperature, battery_level, signal_strength)
    VALUES (%s,%s,%s,%s,%s)
    """

    data = [
        (
            e["device_id"],
            e["timestamp"],
            e["temperature"],
            e["battery_level"],
            e["signal_strength"],
        )
        for e in events
    ]

    cur = conn.cursor()

    execute_batch(cur, query, data)

    conn.commit()

    cur.close()