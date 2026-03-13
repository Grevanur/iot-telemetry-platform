from fastapi import FastAPI
from routers import devices, alerts

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

app.include_router(devices.router)
app.include_router(alerts.router)

Instrumentator().instrument(app).expose(app)