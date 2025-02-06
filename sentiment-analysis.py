from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

classifier = pipeline("sentiment-analysis")

res = classifier("I have been waiting a long time for this course")

print(res)

# Here we are specifying the model name. When we don't specify a model 
# it choses the default model

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# Now we are adding a model and tokenizer name. 
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
res = classifier("I have been waiting a long time for this course")
print(res)
