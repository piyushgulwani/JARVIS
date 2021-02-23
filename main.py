
#! Main Modules 
import pyttsx3 
import wolframalpha
import wikipedia
import webbrowser, os
import time, random
from datetime import datetime
import speech_recognition as sr 
from PIL import ImageGrab
import pytesseract, cv2
import numpy as np
import json, requests


def yourFunctions():

    """
    This function speaks the features of the whole program . 
    """

    speak('My Current Functions are ...')
    functions = """
    Opening Powershell or Command Prompt .
    Wishing or Greeting .
    Telling Time and Day .
    Weather Forecast .
    Wikipedia Searches .
    Shutting or Restarting the System .
    Playing Chrome Dino Game and Edge Surfer
    Intelligent Speech Calculator
    Intelligent Speech Unit Converter
    """
    speak(functions)


def speak(text) :

    """
    The function initializes the audio engine. The arguments should be passed in the string (str) format.
    """
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', -0.2)
    engine.setProperty('volume', 0.5)
    engine.say(text)
    print(text)
    engine.runAndWait()


def client_query(quest) : 
    __api_key = ''
    client = wolframalpha.Client(app_id= __api_key)
    result1 = client.query(quest) 
    result1 = (next(quest.results).text)
    speak(result1)


def wish() :

    """
    As its name tells you it greets the user according to the time. 
    """
    if current_time >= '18:00' and current_time <= '03:30' : 
        speak("Good Evening ")

    elif current_time >= '03:30' and current_time <= '12:00' :
        speak('Good Morning ')

    else : 
        speak('Good Afternoon ')


def command() : 
    """
    The function takes the user voice input and returns as a string which is later stored in a container or variable named query .
    """
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


def current_day() :
    """
    Tells about the current day using the datetime module. 
    Converts the index of the day into the word format
    """
    day_dict = {1: 'Monday', 2: 'Tuesday',  3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'} 
    day = datetime.today().weekday() + 1
    if day in day_dict : 
        day = day_dict[day]
        speak(f"Today is {day}")


def your_name() :
    """
    As its necessary to know your name to your assistant so it grabs your name and stores in the file 
    named name.txt. 
    If the file is deleted or you have changed the  file name the function will create the file again.
    """

    try :
        with open('name.txt', 'r') as f : 
            name = f.readline()
            speak(f'Hello {name} Sir. ')

    except Exception as E : 
        with open('name.txt', 'w') as f : 
            speak('Whats your name Sir ? ')
            name = command()
            name = f.write(name) 
            speak(f'Hello {name} Sir.')


def games() :   
    """
    Play the browser games. Enjoy :)
    """
    speak('Enjoy the game !!')
    webbrowser.open('https://dino-chrome.com/')

def imageToText() : 
    """
    This Function will capture your current screen in real time and detect words. 
    The detected words will later be spoken by the speak function .
    """
    try : 
        while True: 
            capture = ImageGrab.grab()
            tesseract = pytesseract.image_to_string(cv2.cvtColor(np.array(capture), cv2.COLOR_BGR2GRAY), lang='eng')
            speak(tesseract)
            break

    except pytesseract.TesseractNotFoundError : 
        speak('Please setup your python tesseract  !!')

def todaysNews() : 
    """

    """
    try :
        url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='
        news = requests.get(url).text
        news = json.loads(news)
        news = news['articles']
        for i in news : 
            speak(i['title'])
            time.sleep(1)
    
    except Exception as exception2 : 
        speak('Exception Occurred !!')

if __name__ == "__main__":

    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)
    current_time = (f"{hour}:{minute}")

    
    wish()
    your_name()

    try:


        while True :


            query = command().lower()
            if 'powershell'  in query : 
                os.system('start powershell')


            elif 'your functions' in query : 
                yourFunctions()


            elif 'who made you' or 'who is your owner' in query : 
                speak('My Creator is Piyush Gulwani')
                speak('Wanna Reach him')
                opt0 = command()

                if 'yes' in opt0 : 
                    webbrowser.open('https://www.instagram.com/____piiyush____/')

                else : 
                    speak('Thanks')

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


            elif 'games' in query :
                games()


            elif 'shut up' or 'sleep' or 'quit' in query : 
                speak('Sorry to interrupt Sir ')
                quit()


            elif 'wheather' in query : 
                client_query(query)


            elif 'calculate' or 'calculator' in query : 
                speak('Please ask the calculation again ...')
                calculate = command()
                client_query(calculate)

            elif 'unit converter' in query : 
                speak('Enableing Unit Converter. Speak quit to disable it or say the calculation')
                conversion = command().lower()
                if 'quit' or 'exit' in conversion :
                    speak('Quiting the function !!')
                    quit()

                else : 
                    speak('Enabled Unit Conversion')
                    speak('What are the conversions ?')
                    conversion = command().lower()
                    client_query(conversion)

            elif 'read this for me' in query : 
                speak('Reading the page for you !')
                imageToText()

            else : 
                speak("Sorry I didn't understood")

    except KeyboardInterrupt as exception0 :
        speak('User cancelled the request. Quitting !!')
        quit()

    except (ConnectionError or ConnectionAbortedError) as exception1 :
        speak('You aren\'t connected. Quitting !!')
        quit()