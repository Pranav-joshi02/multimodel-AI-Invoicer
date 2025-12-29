from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_model(text[:500])  # limit long text
    return result[0]   # returns {'label':'POSITIVE','score':0.99}
from ocr_reader import extract_text
from text_sentiment import get_sentiment

text = extract_text("../demos/sample_inputs/invoice1.jpg")
print("Sentiment:", get_sentiment(text))
