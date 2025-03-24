import speech_recognition as sr
import os


class AudioSourceManager:
    """Verwaltet verschiedene Audioquellen für die Spracherkennung"""

    @staticmethod
    def get_microphone_source():
        """Liefert eine konfigurierte Mikrofonquelle"""
        return sr.Microphone()

    @staticmethod
    def get_file_source(file_path):
        """
        Liefert eine Audiofile-Quelle
        :param file_path: Pfad zur Audiodatei
        :return: AudioFile Quelle
        :raises: FileNotFoundError wenn Datei nicht existiert
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio-Datei nicht gefunden: {file_path}")
        return sr.AudioFile(file_path)
