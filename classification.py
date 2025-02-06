from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
	"This course is about Donald Trump", 
	candidate_labels=["education", "politics", "business"]
)

print(res)
