# speech_recognition/recognizer.py (aktualisiert)
import os
from .audio_source import AudioSourceManager
import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self, use_google=True):
        self.recognizer = sr.Recognizer()
        self.use_google = use_google

    def recognize_from_microphone(self):
        source = AudioSourceManager.get_microphone_source()
        with source as s:
            print("Bitte sprechen Sie jetzt...")
            audio = self.recognizer.listen(s, timeout=5)
            return self._recognize_audio(audio)

    def recognize_from_file(self, audio_file):
        source = AudioSourceManager.get_file_source(audio_file)
        with source as s:
            audio = self.recognizer.record(s)
            return self._recognize_audio(audio)

    def _recognize_audio(self, audio):
        try:
            if self.use_google:
                return self.recognizer.recognize_google(audio, language="de-DE")
            else:
                return self.recognizer.recognize_sphinx(audio, language="de-DE")
        except sr.UnknownValueError:
            print("Sprache konnte nicht erkannt werden")
            return None
        except sr.RequestError as e:
            print(f"Fehler bei der Spracherkennung: {e}")
            return None
