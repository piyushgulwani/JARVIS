
#! Main Modules 
import pyttsx3 
import wikipedia
import time, os
from datetime import datetime
import speech_recognition as sr 

#! Speaking with Preinting the text 
def speak(text) :
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', -0.2)
    engine.setProperty('volume', 0.5)
    engine.say(text)
    print(text)
    engine.runAndWait()

#! Wisking According to time Using Time
def wish() :
    if current_time >= '18:00' and current_time <= '03:30' : 
        speak("Good Evening ")


    elif current_time >= '03:30' and current_time <= '12:00' :
        speak('Good Morning ')


    else : 
        speak('Good Afternoon ')

#! Voice Input Using SpeechRecognition 
def command() : 

    r = sr.Recognizer()
    with sr.Microphone() as source : 
        speak('Listening...')
        r.pause_threshold = 0.7
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try :

        speak('Hold On ...')
        query = r.recognize_google(audio, language='en-in')
        print(f"Query :/t{query}")
        speak(query)

    except Exception as e : 
        speak('Unexpected Error Occured while Recognizng... Try Again... ')


#! Main code 
if __name__ == "__main__":

    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)
    current_time = (f"{hour}:{minute}")

    wish()

    query = command().lower()

    if 'powershell'  in query : 
        os.system('start powershell')

    if 'command prompt' in query : 
        os.system('start powershell')

    if 'shutdown' in query : 
        os.system('shutdown /s /t 1')

    if 'restart' in query : 
        os.system('shutdown /r /t 1')