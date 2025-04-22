# 🧠 LLM Service - News Summarization & Categorization

This microservice is part of a news aggregator system. It consumes raw news stories from a Kafka topic, processes them using a Large Language Model (LLM) to generate summaries and classify each story by category, and republishes the enriched data to another Kafka topic for downstream services (e.g., storage).

---

## 🛠 Features

- 📰 Summarizes news articles using an LLM
- 🏷️ Categorizes each article into relevant topics
- 🔄 Subscribes to a Kafka topic and republishes processed data
- 🐍 Built with Python, `asyncio`, and Hugging Face Transformers
- 📦 Dockerized for easy deployment
- ⚙️ GitHub Actions CI for pull requests and push to `main` and `dev`

---

## 📦 Tech Stack

- **Python** 3.13
- **Kafka** (consumer & producer)
- **Hugging Face Transformers** for summarization & classification
- **Docker**
- **GitHub Actions** for CI

---

## 🔧 Environment Variables

The `.env` file should contain:

```env
# Kafka
KAFKA_SERVER=localhost
KAFKA_PORT=9094
```
