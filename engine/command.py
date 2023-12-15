import pyttsx3
import speech_recognition as sr
import time
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 0
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        query = r.re(audio, language='en-in')
        print(f"user said: {query}")
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

def allCommands():

    query = takecommand()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)

    else:
        print("not run")
    