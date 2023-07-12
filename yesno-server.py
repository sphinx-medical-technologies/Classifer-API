# uvicorn sentiment-server:app --port 9003 --host 0.0.0.0

from transformers import pipeline
from typing import Union
from fastapi import FastAPI

task = "zero-shot-classification"
model = "facebook/bart-large-mnli"
classifier = pipeline(task, model)

labels = ["yes", "no"]

app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Yes-No-Server'}

@app.get('/yes_or_no/')
async def query_yes_no_analysis(text: str):
    return analyze_yes_no(text)

def analyze_yes_no(text):
	global labels
	return {"result": classifier(text, labels)}
