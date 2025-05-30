import json
from contextlib import contextmanager

from confluent_kafka import Producer

from lib.config.config import KAFKA_PORT, KAFKA_SERVER
from lib.logging.logger import LOGGER

# Kafka configuration
config = {
    "bootstrap.servers": f"{KAFKA_SERVER}:{KAFKA_PORT}",
    "client.id": "scraping-service",
    "acks": "1",
    "retries": 2,
    "compression.codec": "gzip",
}


# Callback function for delivery report
def delivery_report(err, msg):
    if err:
        LOGGER.info(f"Data delivery failed: {err}")
    else:
        message = json.loads(msg.value())
        LOGGER.info(f"Data delivered to {msg.topic()} - {message['title']}")


@contextmanager
def kafka_producer():
    producer = Producer(config)
    try:
        yield producer
    finally:
        producer.flush()
