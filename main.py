
#! Main Modules 
import pyttsx3 
import wolframalpha
import wikipedia
import time, os
from datetime import datetime
import speech_recognition as sr 

#! Telling The Features
def yourFunctions():
    speak('My Current Functions are ...')
    functions = """Opening Powershell or Command Prompt .
    Wishing or Greeting .
    Telling Time and Day .
    Weather Forecast .
    Wikipedia Searches .
    Shutting or Restarting the System .
    """
    speak(functions)

#! Speaking with Preinting the text 
def speak(text) :
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', -0.2)
    engine.setProperty('volume', 0.5)
    engine.say(text)
    print(text)
    engine.runAndWait()

#! Client Query Solving by Wolframalpha
def client_query(quest) : 
    client = wolframalpha.Client(app_id= "Your API")
    result1 = client.query(quest) 
    result1 = (next(quest.results).text)
    speak(result1)

#! Wisking According to time Using Time Module
def wish() :
    if current_time >= '18:00' and current_time <= '03:30' : 
        speak("Good Evening ")

    elif current_time >= '03:30' and current_time <= '12:00' :
        speak('Good Morning ')

    else : 
        speak('Good Afternoon ')


#! Voice Input Using SpeechRecognition Module
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

#! Speaks Current Day using Datetime Module
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

def currentTime() : 
    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)
    current_time = (f"{hour}:{minute}")
    speak(current_time)

#! Main code 
if __name__ == "__main__":

    wish()
    your_name()

    while True :
        query = command().lower()
        if 'powershell'  in query : 
            os.system('start powershell')

        elif 'your functions' in query : 
            yourFunctions()

        elif 'wikipedia' in query : 
            speak('Digging into Wikipedia')
            statement = statement.replace('wikipedia', '')
            result = wikipedia.summary(statement, sentences= 3)
            result = result.split('.')
            speak('Showing Results According to Wikipedia...')
            speak(result)

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
            speak('Sorry to interrupt Sir ')
            quit()

        elif 'wheather' in query : 
            client_query(query)

        else : 
            speak("Sorry I didn't understood")