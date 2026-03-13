# Distributed IoT Telemetry Monitoring Platform

A production-style distributed backend system capable of ingesting and processing telemetry from thousands of IoT devices in real time.

This project demonstrates key backend engineering concepts including:

- Distributed systems
- Event-driven architecture
- High-throughput data ingestion
- Microservices design
- Observability and monitoring

---

# Architecture


A[IoT Device Simulator\n10k–100k async devices] --> B[Kafka Event Stream\nTopic: device.telemetry]

B --> C[Telemetry Ingestion Service\nPython Worker]

C --> D[(PostgreSQL\nTelemetry Storage)]
C --> E[(Redis Cache\nLatest Device State)]

C --> F[Alert Engine]

F --> G[Kafka Topic\n device.alerts]

D --> H[FastAPI Backend API]
E --> H

H --> I[Client Applications / Dashboard]

H --> J[Prometheus Metrics]
J --> K[Grafana Dashboards]

System Components
1. IoT Device Simulator

Simulates thousands of devices sending telemetry events asynchronously.

Each device produces:

device_id

timestamp

temperature

battery_level

signal_strength

Designed using asyncio to simulate large scale device networks.

2. Kafka Streaming Pipeline

Kafka acts as the event backbone for the system.

Topics used:

device.telemetry
device.alerts

Benefits:

High throughput

Fault-tolerant event streaming

Decoupled microservices

3. Telemetry Ingestion Service

Consumes telemetry events from Kafka and processes them.

Responsibilities:

Validate device events

Detect anomalies

Store telemetry in PostgreSQL

Cache device state in Redis

Batch database writes for high throughput

4. Alert Engine

Processes telemetry streams and generates alerts for abnormal conditions.

Examples:

High temperature

Low battery

Signal loss

Alert events are published to Kafka.

5. Backend API Service

Built using FastAPI.

Provides endpoints:

GET /devices
GET /devices/{device_id}
GET /devices/{device_id}/telemetry
GET /alerts

Uses:

Redis for fast lookups

PostgreSQL for persistent telemetry data

6. Monitoring and Observability

The system includes a full monitoring stack.

Prometheus

Collects metrics such as:

API request latency

request throughput

system performance

Grafana

Provides dashboards for visualizing system metrics.

Technology Stack
Layer	Technology
Backend API	FastAPI
Streaming	Apache Kafka
Cache	Redis
Database	PostgreSQL
Monitoring	Prometheus + Grafana
Infrastructure	Docker
Language	Python
Project Structure
iot-telemetry-platform/

device_simulator/
    simulator.py

ingestion_service/
    main.py
    kafka_consumer.py
    postgres_db.py
    redis_cache.py

alert_engine/
    alert_service.py
    kafka_producer.py
    alert_rules.py

api_service/
    main.py
    db.py
    routers/

monitoring/
    prometheus.yml

infrastructure/
    docker-compose.yml

scripts/
    load_test.py
Running the System
1. Start Infrastructure
cd infrastructure
docker-compose up -d

This starts:

Kafka

Zookeeper

PostgreSQL

Redis

Prometheus

Grafana

2. Create Kafka Topic
docker exec -it kafka kafka-topics \
--create \
--topic device.telemetry \
--bootstrap-server localhost:9092 \
--partitions 6 \
--replication-factor 1
3. Setup Python Environment
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install kafka-python fastapi uvicorn redis psycopg2-binary prometheus-fastapi-instrumentator
4. Start Services

Open multiple terminals.

Device Simulator
python device_simulator/simulator.py

Telemetry Ingestion
python ingestion_service/main.py

Alert Engine
python alert_engine/alert_service.py

API Service
uvicorn api_service.main:app --reload

Access Services
Service	URL
API	http://localhost:8000/docs
Prometheus	http://localhost:9090
Grafana	http://localhost:3000

Grafana login:
admin
admin

Performance Design
The system is designed to handle high throughput using:
Kafka event streaming
Async device simulation
Batched database writes

Redis caching
This architecture supports tens of thousands of device events per second.
Key Engineering Concepts Demonstrated
Event-driven architecture
Distributed message queues

Microservices
Data ingestion pipelines
High-throughput backend systems
Observability and monitoring


Future Improvements
Possible extensions:

Kubernetes deployment
Kafka partitioning strategy
WebSocket real-time dashboards
Device authentication
Machine learning anomaly detection


Author

Gowtham Revanur
Graduate Student
Computer Science
Georgia State University