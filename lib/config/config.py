import os

from dotenv import load_dotenv

load_dotenv()

KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9094")
KAFKA_PRODUCER_TOPIC = os.getenv("KAFKA_PRODUCER_TOPIC", "processed-data")
KAFKA_CONSUMER_TOPIC = os.getenv("KAFKA_CONSUMER_TOPIC", "news-data")
