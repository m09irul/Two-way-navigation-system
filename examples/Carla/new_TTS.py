# speech.py
import multiprocessing
import pyttsx3

def speak_text(command):
    engine = pyttsx3.init()
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 30)  # Adjust the rate of speech
    engine.setProperty('voice', voice_id)
    engine.say(command)
    engine.runAndWait()

def speak(msg):
    # Create a Process for the message
    p = multiprocessing.Process(target=speak_text, args=(msg,))
    p.start()  # Starts the process
    p.join()  # Waits for process to complete

    
