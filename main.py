from speech_recog.recognizer import SpeechRecognizer
from sentiment_analysis.analyzer import SentimentAnalyzer
import time

def show_menu():
    """Zeigt das Hauptmenü an und gibt die Benutzerauswahl zurück"""
    print("\n" + "=" * 40)
    print("HAUPTMENÜ - SPRACHERKENNUNG & SENTIMENT-ANALYSE")
    print("=" * 40)
    print("1. Sprache live über Mikrofon aufnehmen")
    print("2. Sprache aus Audiodatei erkennen")
    print("3. Einstellungen ändern")
    print("4. Programm beenden")
    print("=" * 40)

    while True:
        choice = input("Ihre Auswahl (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Ungültige Eingabe! Bitte 1-4 wählen.")

def settings_menu(current_settings, analyzer):
    """Erweitertes Einstellungsmenü"""
    print("\n" + "-" * 40)
    print("EINSTELLUNGEN")
    print("-" * 40)
    print(f"1. Spracherkennungsmodus: {'Google (online)' if current_settings['online'] else 'Sphinx (offline)'}")
    print(f"2. Analyse-Sprache: {'Deutsch' if current_settings['language'] == 'de' else 'Englisch'}")
    print("3. Zurück zum Hauptmenü")
    print("-" * 40)

    choice = input("Ihre Auswahl (1-3): ")
    if choice == "1":
        current_settings["online"] = not current_settings["online"]
        mode = "Google (online)" if current_settings["online"] else "Sphinx (offline)"
        print(f"\nSpracherkennungsmodus geändert zu: {mode}")
    elif choice == "2":
        lang = 'en' if current_settings['language'] == 'de' else 'de'
        if analyzer.set_language(lang):
            current_settings['language'] = lang
            print(f"\nAnalyse-Sprache geändert zu: {'Deutsch' if lang == 'de' else 'Englisch'}")
    time.sleep(1)
    return current_settings

def main():
    # Standard-Einstellungen
    settings = {
        'online': True,
        'language': 'de'
    }

    recognizer = SpeechRecognizer(use_google=settings['online'])
    analyzer = SentimentAnalyzer()

    while True:
        choice = show_menu()

        # Live-Aufnahme
        if choice == "1":
            print("\nLive-Aufnahme startet... (STRG+C zum Abbrechen)")
            try:
                text = recognizer.recognize_from_microphone()
                if text:
                    result = analyzer.analyze(text)
                    print(f"\nErgebnis ({result['language']}):")
                    print(f"Sentiment: {result['sentiment']}")
                    print(f"Konfidenz: {result['confidence']:.2%}")
            except KeyboardInterrupt:
                print("\nAufnahme abgebrochen")
            except Exception as e:
                print(f"Fehler: {e}")
            input("\nDrücken Sie Enter um fortzufahren...")

        # Audiodatei verarbeiten
        elif choice == "2":
            audio_path = input("\nGeben Sie den Pfad zur Audiodatei an: ").strip('"')
            try:
                text = recognizer.recognize_from_file(audio_path)
                if text:
                    result = analyzer.analyze(text)
                    print(f"\nErgebnis ({result['language']}): {text}")
                    print(f"Sentiment: {result['sentiment']}")
                    print(f"Konfidenz: {result['confidence']:.2%}")
            except FileNotFoundError:
                print("Fehler: Datei nicht gefunden!")
            except Exception as e:
                print(f"Fehler: {e}")
            input("\nDrücken Sie Enter um fortzufahren...")

        # Einstellungen
        elif choice == "3":
            settings = settings_menu(settings, analyzer)
            recognizer = SpeechRecognizer(use_google=settings['online'])

        # Beenden
        elif choice == "4":
            print("\nProgramm wird beendet...")
            break

if __name__ == "__main__":
    main()