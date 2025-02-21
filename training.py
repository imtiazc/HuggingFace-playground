# Training a data set

from transformers import AutoTokenizer
from datasets import load_dataset

# Load the IMDB data set
dataset = load_dataset("imdb")

# Preprocess the data
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
