from transformers import AutoTokenizer

"""
How a tokenizer works
"""

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# seq = "Using a transformer network is simple"
seq = "Zayden is a smart kid who likes computer games, music and art."
print("OG string: ", seq)
# Shows how token are represented as numerical tokens and their attention values
result = tokenizer(seq)
print(result)

# Prints tokens in English
tokens = tokenizer.tokenize(seq)
print(tokens)

ids = tokenizer.convert_tokens_to_ids(tokens)
print("ids: ", ids)

# decoding from ids
decoded_string = tokenizer.decode(ids)
print("decoded:", decoded_string)

