import torch
from transformers import pipeline

tagger = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def generate_tags(text):
    candidate_labels = [
        "health", "finance", "education", "climate", "sports",
        "politics", "entertainment", "technology", "transportation", "agriculture"
    ]
    result = tagger(text, candidate_labels)
    top_tags = result["labels"][:3]
    return ", ".join(top_tags)
