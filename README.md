
A scalable data streaming pipeline that:
1. Creates user data through a REST API
2. Streams the data using Apache Kafka
3. Stores data in both SQL and NoSQL databases for different use cases

## Features

- **REST API**: Create and manage user data
- **Real-time Streaming**: Apache Kafka for reliable data transportation
- **Dual Database Storage**:
  - SQL Database (PostgreSQL) for structured queries
  - NoSQL Database (MongoDB) for flexible schema
- **Dockerized**: Easy deployment with Docker containers

## Architecture Overview
API Server → Kafka Producer →  Kafka Consumers → SQL & NoSQL Databases


## Technology Stack

| Component       | Technology Options |
|----------------|-------------------|
| API Framework  | FastAPI/Flask/Django |
| Message Broker | Apache Kafka |
| SQL Database   | PostgreSQL |
| NoSQL Database | MongoDB |
| Containerization | Docker |
| Orchestration  | Docker Compose |

## Prerequisites

- Docker 20.10+
- Docker Compose 1.29+
- Python 3.8+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alrSasani/Docker_kafka_app.git
cd Docker_kafka_app```

docker-compose up --build 
```
