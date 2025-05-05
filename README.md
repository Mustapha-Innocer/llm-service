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

## 🧪 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/Mustapha-Innocer/llm-service.git
cd llm-service
```

### 2. Create `.env` file with the appropriate values
```ini
# Kafka
KAFKA_SERVER=localhost
KAFKA_PORT=9094
KAFKA_PRODUCER_TOPIC=processed-data
KAFKA_CONSUMER_TOPIC=news-data
```

### 3. Create new python virtual environment
```bash
python -m venv venv
```

### 4. Intall the python dependencies
```bash
pip install -r requirements.txt
```

### 5. Run
```bash
python main.py
```

---

## 🧱 Related Services

This is part of a larger microservice-based system. See the [Main Project README](https://github.com/Mustapha-Innocer/news-aggregator) for architecture and links to all services.
