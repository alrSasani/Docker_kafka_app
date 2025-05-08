# Data Streaming Pipeline: API to Databases via Kafka

![Pipeline Architecture](architecture-diagram.png) *(Optional: Add diagram if available)*

A scalable data streaming pipeline that:
1. Creates user data through a REST API
2. Streams the data using Apache Kafka
3. Stores data in both SQL and NoSQL databases for different use cases

## Features

- **REST API**: Create and manage user data
- **Real-time Streaming**: Apache Kafka for reliable data transportation
- **Dual Database Storage**:
  - SQL Database (PostgreSQL/MySQL) for structured queries
  - NoSQL Database (MongoDB/Cassandra) for flexible schema
- **Dockerized**: Easy deployment with Docker containers

## Architecture Overview
API Server → Kafka Producer → Kafka Cluster → Kafka Consumers → SQL & NoSQL Databases


## Technology Stack

| Component       | Technology Options |
|----------------|-------------------|
| API Framework  | FastAPI/Flask/Django |
| Message Broker | Apache Kafka |
| SQL Database   | PostgreSQL/MySQL |
| NoSQL Database | MongoDB/Cassandra |
| Containerization | Docker |
| Orchestration  | Docker Compose |

## Prerequisites

- Docker 20.10+
- Docker Compose 1.29+
- Python 3.8+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-streaming-pipeline.git
cd data-streaming-pipeline
Set up environment variables:

bash
cp .env.example .env
# Edit the .env file with your configuration
Start the services:

bash
docker-compose up -d
Configuration
Configure the services in .env file:

ini
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Kafka Configuration
KAFKA_BROKERS=kafka:9092
KAFKA_TOPIC=user_data

# Database Configuration
POSTGRES_URL=postgresql://user:pass@db:5432/appdb
MONGO_URL=mongodb://user:pass@mongo:27017/appdb
Usage
Create user data through API:

bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com"}'
Verify data in databases:

SQL: Connect to PostgreSQL and query users table

NoSQL: Connect to MongoDB and check users collection

Development
To run in development mode:

bash
docker-compose -f docker-compose.dev.yml up --build
Monitoring
Access these services while running:

API Docs: http://localhost:8000/docs (if using FastAPI)

Kafka UI: http://localhost:8080 (if configured)

PGAdmin: http://localhost:5050 (if configured)

License
MIT License


**Recommendations to enhance your README:**
1. Add an architecture diagram (create one with [draw.io](https://app.diagrams.net/))
2. Include sample API responses
3. Add a "Contributing" section if open source
4. Add health check endpoints if available
5. Include logging/monitoring details