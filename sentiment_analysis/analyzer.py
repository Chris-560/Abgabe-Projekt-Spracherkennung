from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.models = {
            'de': {
                'model': "oliverguhr/german-sentiment-bert",
                'labels': {
                    "negative": "negativ",
                    "neutral": "neutral",
                    "positive": "positiv"
                }
            },
            'en': {
                'model': "distilbert-base-uncased-finetuned-sst-2-english",
                'labels': {
                    "NEGATIVE": "negativ",
                    "POSITIVE": "positiv"
                }
            }
        }
        self.language = 'de'  # Standardsprache
        self.analyzer = None
        self._load_model()

    def _load_model(self):
        config = self.models[self.language]
        self.analyzer = pipeline(
            "text-classification",
            model=config['model'],
            return_all_scores=False
        )

    def set_language(self, lang):
        """Setzt die Analyse-Sprache (de/en)"""
        if lang in self.models:
            self.language = lang
            self._load_model()
            return True
        return False

    def analyze(self, text):
        if not text:
            return None

        try:
            result = self.analyzer(text)[0]
            label_map = self.models[self.language]['labels']
            return {
                'sentiment': label_map.get(result['label'], result['label']),
                'confidence': result['score'],
                'language': self.language.upper()
            }
        except Exception as e:
            print(f"Analysefehler: {e}")
            return None