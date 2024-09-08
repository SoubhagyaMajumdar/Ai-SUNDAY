import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    eel.DisplayMessage(text)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 10)
    
    try:
        print('Recognizing')
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        return ""
    
    return query.lower()
    
@eel.expose
def allCommands():
        query = takecommand()
        print(query)

        if "open" in query:
            from Engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from Engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("Not run")
