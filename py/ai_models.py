import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from sentence_transformers import SentenceTransformer
import numpy as np

class AIModelManager:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.models = {
            'sentiment': self._load_sentiment_model(),
            'embeddings': SentenceTransformer('all-MiniLM-L6-v2')
        }
    
    def _load_sentiment_model(self):
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    
    def analyze_sentiment(self, text):
        return self.models['sentiment'](text)
    
    def get_embeddings(self, text):
        return self.models['embeddings'].encode(text)