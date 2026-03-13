from fastapi import APIRouter
import psycopg2

router = APIRouter()

conn = psycopg2.connect(
    host="postgres",
    database="telemetry",
    user="admin",
    password="admin"
)


@router.get("/alerts")
def get_alerts():

    cur = conn.cursor()

    cur.execute("SELECT * FROM alerts LIMIT 100")

    rows = cur.fetchall()

    return rows