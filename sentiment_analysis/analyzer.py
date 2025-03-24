from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis", 
            model="distilbert-base-multilingual-cased"
        )
        self.label_map = {
            "POSITIVE": "positiv",
            "NEGATIVE": "negativ",
            "NEUTRAL": "neutral"
        }
    
    def analyze(self, text):
        if not text:
            return None
        
        result = self.analyzer(text)[0]
        label = result['label']
        score = result['score']
        german_label = self.label_map.get(label, label)
        
        print(f"Sentiment: {german_label} (Wahrscheinlichkeit: {score:.2f})")
        return german_label, score