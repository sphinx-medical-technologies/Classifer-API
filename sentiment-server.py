# uvicorn sentiment-server:app --port 9003 --host 0.0.0.0

from transformers import pipeline
from typing import Union
from fastapi import FastAPI

task = "zero-shot-classification"
model = "facebook/bart-large-mnli"
classifier = pipeline(task, model)

labels = ["yes", "no"]

nlp = pipeline(task='sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Sentiment-Server'}

@app.get('/yes_or_no/')
async def query_yes_no_analysis(text: str):
    return analyze_yes_no(text)

def analyze_yes_no(text):
	global labels
	return {"result": classifier(text, labels)}

@app.get('/sentiment_analysis/')
async def query_sentiment_analysis(text: str):
    return analyze_sentiment(text)

def analyze_sentiment(text):
    """Get and process result"""

    result = nlp(text)

    sent = ''
    if (result[0]['label'] == '1 star'):
        sent = 'very negative'
    elif (result[0]['label'] == '2 star'):
        sent = 'negative'
    elif (result[0]['label'] == '3 stars'):
        sent = 'neutral'
    elif (result[0]['label'] == '4 stars'):
        sent = 'positive'
    else:
        sent = 'very positive'

    prob = result[0]['score']

    # Format and return results
    return {'sentiment': sent, 'probability': prob}
