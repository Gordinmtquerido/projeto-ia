from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import threading

app = Flask(__name__)
CORS(app)

# Carregar modelos (fazer apenas uma vez)
sentiment_analyzer = None
embedding_model = None
models_lock = threading.Lock()

def load_models():
    global sentiment_analyzer, embedding_model
    with models_lock:
        if sentiment_analyzer is None:
            sentiment_analyzer = pipeline("sentiment-analysis", 
                                       model="distilbert-base-uncased-finetuned-sst-2-english")
        if embedding_model is None:
            embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    load_models()
    
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Análise de sentimento
        sentiment_result = sentiment_analyzer(text)[0]
        
        # Embeddings
        embeddings = embedding_model.encode(text)
        
        # Palavras-chave simples (implementação básica)
        words = [word for word in text.split() if len(word) > 3]
        keywords = list(set(words))[:3]  # Remove duplicatas e pega as 3 primeiras
        
        return jsonify({
            "sentiment": sentiment_result['label'],
            "sentiment_score": sentiment_result['score'],
            "keywords": keywords,
            "word_count": len(text.split()),
            "char_count": len(text),
            "embeddings": embeddings.tolist()[:10]  # Retorna apenas os primeiros 10 valores
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)