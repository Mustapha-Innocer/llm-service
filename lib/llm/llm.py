import transformers as trfs

from lib.logging.logger import LOGGER

# Load the model and tokenizer for summarization
summarizer = trfs.pipeline("summarization", model="facebook/bart-large-cnn")

# Load the model and tokenizer for text classification
model_name = "ilsilfverskiold/classify-news-category-iptc"
tokenizer = trfs.AutoTokenizer.from_pretrained(model_name)
model = trfs.AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = trfs.pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
)


async def summerize(data):
    LOGGER.info("Summarizing the the story")
    res = summarizer(
        data["body"],
        max_length=120,
        min_length=100,
        do_sample=False,
    )
    data["summary"] = res[0]["summary_text"]


async def categorize(data):
    LOGGER.info("Categorizing the story")
    res = classifier(
        data["body"],
        top_k=1,
        truncation=True,
        padding=True,
        max_length=512,
    )
    data["category"] = res[0]["label"]
