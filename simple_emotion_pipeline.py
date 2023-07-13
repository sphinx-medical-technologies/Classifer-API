# -*- coding: utf-8 -*-
"""simple_emotion_pipeline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q5bBNe7gIqcs6uUtwoTyaHwQ8nk3xCoZ
"""

!pip install transformers

from transformers import pipeline

classifier1 = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

classifier1("I have pain in my left foot")

classifier2 = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", return_all_scores=True)

classifier2("I have pain in my left foot")

classifier3 = pipeline("text-classification", model="Narshion/bert-base-multilingual-cased-urgency", return_all_scores=True)

classifier3("I have pain in my left foot")

classifier3 = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment", return_all_scores=True)

classifier3("I have pain in my left foot")