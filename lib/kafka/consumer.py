from lib.config.config import KAFKA_PORT, KAFKA_SERVER
from confluent_kafka import Consumer

# Kafka configuration
config = {
    "bootstrap.servers": f"{KAFKA_SERVER}:{KAFKA_PORT}",
    "auto.offset.reset": "earliest",
    "group.id": "llm-service",
    'enable.auto.commit': False
}

consumer = Consumer(config)
