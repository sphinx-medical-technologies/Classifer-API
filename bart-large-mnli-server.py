# uvicorn bart-large-mnli-server:app --port 9004 --host 0.0.0.0

from fastapi import FastAPI, Query
from transformers import pipeline
from typing import List

app = FastAPI()

classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli",
                      framework="pt") 

@app.get('/')
def get_root():
    return {'message': 'Text-Classifier-Server'}

@app.get("/classify")
def classify_text(text: str, 
                  categories: List[str] = Query(None)):
    
    return classifier(text, candidate_labels=categories)

# if __name__ == "__main__":
#    import uvicorn
#
#    uvicorn.run(app, host="0.0.0.0", port=8000)
