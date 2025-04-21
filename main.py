import asyncio
import json

from lib.kafka.consumer import consumer
from lib.kafka.producer import delivery_report, kafka_producer
from lib.llm.llm import categorize, summerize
from lib.logging.logger import LOGGER


async def heartbeat():
    while True:
        LOGGER.info("Heartbeat received ...")
        await asyncio.sleep(5)


async def consume():
    consumer.subscribe(["news-data"])
    while True:
        try:
            msg = consumer.poll(5)

            if msg is None:
                LOGGER.info("No new message in the queue")
                await asyncio.sleep(30)
                continue

            if msg.error():
                LOGGER.error(f"Consumer error: {msg.error()}")
                continue

            data = json.loads(msg.value().decode("utf-8"))
            LOGGER.info(f"Received new strory: {data["url"]}")
            await asyncio.gather(summerize(data), categorize(data))
            consumer.commit()

            with kafka_producer() as producer:
                producer.produce(
                    topic="processed-data",
                    value=json.dumps(data),
                    callback=delivery_report,
                )
        except Exception as e:
            LOGGER.error(f"Unable to process {data["url"]}: {e}")
            await asyncio.sleep(30)


async def main():
    await asyncio.gather(heartbeat(), consume())


if __name__ == "__main__":
    LOGGER.info(f"{'*' * 10} Starting LLM Service {'*' * 10}")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOGGER.info(f"{'*' * 10} LLM Service closed {'*' * 10}")
