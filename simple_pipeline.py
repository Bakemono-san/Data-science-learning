from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("oui bien sur on l'a fait nous meme")

print(res)
