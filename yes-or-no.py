from transformers import pipeline
from typing import Union
from fastapi import FastAPI

# Yes
# Sure
# Okay
# Yeah
# Certainly
# Yes I do
# Yeah, sure
# Yep
# Cool
# definitely
# of course
# naturally
# that’s right
# by all means
# you bet
# you’re on
# yea
# sweet
# yep
# totally
# totes
# K
# Okie dokie
# Alright
# Alrighty
# sounds good
# for sure
# sure thing
# Definitely
# Of course
# Yeah, yeah, yeah
# fine
# Obviously
# Mhmm
# Uh-huh
# I think so

# No
# Nope
# Nah
# No way
# No thanks
# No thank you
# I don’t think so
# Uh-uh
# Uh-no

yes_test_text = "for sure"
no_test_text = "no way"

task = "zero-shot-classification"
model = "facebook/bart-large-mnli"
classifier = pipeline(task, model)

labels = ["yes", "no"]

result = classifier(yes_test_text, labels)
print(result)

result = classifier(yes_test_text, labels)
print(result["labels"][0])
print(result["scores"][0])

result = classifier(no_test_text, labels)
print(result)

result = classifier(no_test_text, labels)
print(result["labels"][0])
print(result["scores"][0])

app = FastAPI()

@app.get("/")
def read_root():
    return {"Yes": "No"}

@app.get("/yes-or-no")
def read_item(text: Union[str, None] = None):
	global labels
	return {"result": classifier(text, labels)}

