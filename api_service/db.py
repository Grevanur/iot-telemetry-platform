import psycopg2
import redis

# PostgreSQL connection
def get_postgres_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="telemetry",
        user="admin",
        password="admin",
        port=5432
    )
    return conn


# Redis connection
def get_redis_client():
    r = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    return r