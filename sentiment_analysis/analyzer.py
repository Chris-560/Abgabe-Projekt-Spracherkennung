from transformers import pipeline

from transformers import AutoConfig

model_name = "distilbert-base-multilingual-cased"
config = AutoConfig.from_pretrained(model_name)
print("Exakte Label-Zuordnung:", config.id2label)

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis", 
            model="distilbert-base-multilingual-cased"
        )
        self.label_map = {
            "LABEL_0": "negativ",
            #"LABEL_1": "neutral",
            "LABEL_1": "positiv"
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