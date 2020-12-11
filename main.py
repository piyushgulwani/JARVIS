
#! Main Modules 
import pyttsx3 
import shutil
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
        r.phrase_threshold = 0.5
        r.non_speaking_duration = 0.4
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try :

        speak('Hold On ...')
        query = r.recognize_google(audio, language='en-in')
        print(f"Query :\t{query}")

    except Exception as e : 
        speak('Unexpected Error Occurred while Recognizing... Try Again... ')
        
    return query 

#! Speaks Current Day
def current_day() :
    day_dict = {1: 'Monday', 2: 'Tuesday',  3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'} 
    day = datetime.today().weekday() + 1
    if day in day_dict : 
        day = day_dict[day]
        speak(f"Today is {day}")


#! This Function  will Run only Once 
def your_name() :
    try :
        with os.open('name.txt', 'r') as f :
            name = f.readline()
            speak(f'Your Good name is {name}. So I will call You {name}')

    except FileNotFoundError :
        with os.open('name.txt', 'w') as f :
            speak('What Should I call You?')
            name = command()
            f.write(name)
            speak(f'Your Good name is {name}. So I will call You {name}')


#! Main code 
if __name__ == "__main__":

    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)
    current_time = (f"{hour}:{minute}")

    wish()
    your_name()
    while True :
        query = command().lower()
        if 'powershell'  in query : 
            os.system('start powershell')

        elif 'command prompt' in query : 
            os.system('start cmd')

        elif 'shutdown' in query : 
            os.system('shutdown /s /t 1')

        elif 'restart' in query : 
            os.system('shutdown /r /t 1')

        elif 'the time' in query : 
            speak(current_time) 
        
        elif 'the day' in query : 
            current_day()

        elif 'shut up' or 'sleep' or 'quit' in query : 
            speak('Sorry to interrupt Quitting')
            quit()

        else : 
            speak("Sorry I didn't understood")