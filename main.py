
#! Main Modules 
import pyttsx3 
import wolframalpha
import wikipedia
import webbrowser, os
import winshell
import time, random
from datetime import datetime
import speech_recognition as sr 
from PIL import ImageGrab
import pytesseract, cv2
import numpy as np
import pyjokes
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
    __api_key = '45EXYP-Q56VVHXWUE'
    client = wolframalpha.Client(app_id= __api_key)
    result1 = client.query(quest) 
    answers = next(quest.Results).text
    speak(answers)


def wish() :

    """
    As its name tells you it greets the user according to the time. 
    """
    try :
        if currentTime >= '18:00' and currentTime <= '03:30' : 
            speak("Good Evening ")

        if currentTime >= '03:30' and currentTime <= '12:00' :
            speak('Good Morning ')

        else : 
            speak('Good Afternoon ')
            
    except Exception as exception5 :
        speak('Quitting !! Thanks')

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

    except Exception as exception4 : 
        with open('name.txt', 'w') as f : 
            speak('Whats your name Sir ? ')
            name = command()
            if len(name) > 7 : 
                speak('Name cannot exceed beyond 7')

            else  : 
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

    clear = lambda: os.system('cls')

    try:

        wish()
        your_name()


        while True :


            query = command().lower()
            if 'powershell'  in query : 
                os.system('start powershell')


            elif 'your functions' in query : 
                yourFunctions()


            elif  'open youtube' in query : 
                speak('Surfing  to  Youtube !!')
                webbrowser.open('www.youtube.com')


            elif 'open google' in query : 
                speak('Surfing  to  Google !!')
                webbrowser.open('www.google.com')


            elif  'open stack overflow' in query : 
                speak('Surfing  to  Stack Overflow  !!')
                webbrowser.open('www.stackoverflow.com')

            elif 'open github' in  query : 
                speak('Surfing  to  Github !!')
                webbrowser.open('www.github.com')


            elif 'jokes' in query : 

                for i in pyjokes.get_jokes() : 
                    if i <= 10 : 
                        speak(i)
                        continue
                    else : 
                        break


            elif 'who made you' in query : 
                speak('My Creator is Piyush G')
                speak('Wanna Reach him')
                opt0 = command()

                if 'yes' in opt0 : 
                    webbrowser.open('https://www.instagram.com/____piiyush____/')
                    break

                else :
                    speak('Thanks')
                    break

            elif 'wikipedia' in query : 
                speak('Digging into Wikipedia')
                statement = query.replace('wikipedia', '')
                result = wikipedia.summary(statement, sentences= 3)
                speak('Showing Results According to Wikipedia...')
                speak(result)


            elif 'command prompt' in query : 
                os.system('start cmd')


            elif 'who is' in query or 'what is' in query : 
                client_query(query)

            elif 'shutdown' in query : 
                os.system('shutdown /s /t 1')


            elif 'restart' in query : 
                os.system('shutdown /r /t 1')


            elif 'the time' in query : 
                currentTime = datetime.strftime('#H : #M')
                speak(f'Current time is {currentTime}')

            elif 'the day' in query : 
                current_day()

            elif 'your work' in query :
                speak('My work is to automate small tasks')


            elif 'games' in query :
                games()


            elif 'shut up' or 'sleep' or 'quit' in query : 
                speak('Quitting !! Sorry. ')
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


                else : 
                    speak('Enabled Unit Conversion')
                    speak('What are the conversions ?')
                    conversion = command().lower()
                    client_query(conversion)


            elif 'read this for me' in query : 
                speak('Reading the page for you !')
                imageToText()


            elif 'todays news' or 'news' in query : 
                todaysNews()


            elif 'i love you' in query : 
                speak('Its hard to understand')


            elif 'empty recycle bin' in query : 
                winshell.recycle_bin.empty(confirm = False, show_progress = True, sound = True)
                speak('Successfully emptied the bin !!')


            elif 'your age' in query : 
                speak('Program doesn\'t have age :(')


            else : 
                speak("Sorry I didn't understood")


    except KeyboardInterrupt as exception0 :
        speak('User cancelled the request. Quitting !!')
        quit()