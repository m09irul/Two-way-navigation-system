# b.py
from new_TTS import speak

if __name__ == "__main__":
    for i in range(0,10):
        speak("Hello, world!")
        if i > 5:
            speak("I'm speaking again!")
