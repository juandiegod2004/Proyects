import speech_recognition as sr 
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer



name = "kiddo"
listener = sr. Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def listen():
    listener = sr.Recognizer()     
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
        return ''  # Devolver una cadena vacía en caso de error
    return rec

def run_kiddo():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No te entendí, intenta de nuevo")
            continue     
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            engine.say("Reproduciendo " + music)
            engine.runAndWait()
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            engine.say(wiki)
            engine.runAndWait()

if __name__ == '__main__':
    run_kiddo()
