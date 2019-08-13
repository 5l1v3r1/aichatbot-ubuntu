import speech_recognition as sr
import os
import random
import sys
import time
import datetime
import webbrowser
import pyaudio
import pyttsx3
import requests
import json
import wikipedia
import wolframalpha
import urllib3
from playsound import playsound
#need to install win32api .. pip install pywin32
import pyjokes

urllib3.disable_warnings()
client = wolframalpha.Client('G8V8UW-XQ5G66R4UV')

#api key for openweather
api_key="9db935f24bmsh30aaa484f3eac45p196abbjsn03558978c159"
base_url="http://api.openweathermap.org/data/2.5/weather?"
#complete_url = base_url + "appid=" + api_key + "&q=" + "Thanjavur"
complete_url="http://api.openweathermap.org/data/2.5/weather?lat=13.30&lon=80.16&APPID=8f605c186309e3d8f60bb7b2f31ba75c&units=metric"
response = requests.get(complete_url)
x=response.json()

#weather
if x["cod"] != "404":
    main = x["main"]
    wind = x["wind"]
    weather = x["weather"]
    description = weather[0]["description"]
    current_temp = main["temp"]
    max_temp = main["temp_max"]
    min_temp = main["temp_min"]
    humidity = main["humidity"]
    windspeed = wind["speed"]

#print response
#print(x)


try:
    engine = pyttsx3.init('espeak')
except ImportError:
    print("Driver Not Found")
except RuntimeError:
    print("Driver Failed Initialize")
'''    
#to get voices in windows
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
'''

engine.setProperty('voice','')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

'''
#test_voice
engine.say("Hello Sir..")
engine.runAndWait()
'''

speech =sr.Recognizer()



def speak(command):
    print("S.P.A.M :"+command)
    engine.say(command)
    engine.runAndWait()

def voice_command():

    catt=""
    print("Listening...")
    try:
        #catt - coverted audio to text
        with sr.Microphone() as inputaudio:
            speech.pause_threshold=1
            speech.adjust_for_ambient_noise(inputaudio, duration=1)
            audio = speech.listen(source=inputaudio,timeout=5,phrase_time_limit=5)
        catt = speech.recognize_google(audio)
        print('User: ' + catt + '\n')

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("Check Your Internet Sir..")
    except sr.WaitTimeoutError:
        speak("Sorry..Sir I Could Not Catch You")
    return catt

def wishInTime():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak("Good Morning Sir..Have a nice day!")

    if currentH >= 12 and currentH < 18:
        speak("Good Afternoon Sir!")

    if currentH >= 18 and currentH !=0:
        speak("Good Evening Sir!")


currentDT = datetime.datetime.now()
a=currentDT.strftime("%a,%b %d,%Y")
cd=str(a)
b=currentDT.strftime("%I:%M:%S %p")
ct=str(b)



def assistant():

    while True:

        voice_input = voice_command()

        if "hi buddy" in voice_input or "hey assistant" in voice_input or "assistant" in voice_input or "hello" in voice_input or "still alive" in voice_input \
                or "still awake" in voice_input or "spam" in voice_input or "hey spam" in voice_input:
            randomtext = ["Yes Sir....How Can I Help You?", "Yes Sir..Im Responding!", "Aldready there Sir!!",
                          "Give a command Sir!"]
            speak(random.choice(randomtext))

        elif "open youtube" in voice_input or "youtube" in voice_input or "show youtube" in voice_input or "open YouTube" in voice_input:
            speak("Okay sir..Showing you Youtube")
            webbrowser.get('firefox').open('www.youtube.com')

        elif "open google" in voice_input or "open Google" in voice_input or "google me" in voice_input or "show google" in voice_input:
            speak("Okay Sir!..Opening Google.com")
            webbrowser.get('firefox').open('www.google.co.in')

        elif "github" in voice_input or "open gitHub" in voice_input:
            speak("Okay Sir! Got It")
            webbrowser.get('firefox').open('www.github.com')

        elif "shutdown" in voice_input or "kill yourself" in voice_input or "good bye" in voice_input or "see you later" in voice_input or "goodbye" in voice_input:
            speak("Ok Sir..!Call me if you need an assist")
            sys.exit()

        elif "sleep mode" in voice_input or "go to sleep" in voice_input or "good night" in voice_input:
            randomtext = ["Good Night", "Bye Bye Sir!", "Call me when you need Sir!", "I will take some rest Sir"]
            speak(random.choice(randomtext))
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif "show time" in voice_input or "time" in voice_input or "what's the time" in voice_input or "present time" in voice_input or "current time" in voice_input:
            speak(ct)

        elif "show date" in voice_input or "date" in voice_input or "todays date" in voice_input or "current date" in voice_input or "present date" in voice_input:
            speak(cd)

        elif "weather" in voice_input or "show weather" in voice_input or "tell me about weather" in voice_input:
            speak("Here is a quick overview of current weather.\n The temperature is at " + str(current_temp) +"degrees.\n"+" Possible maximum temperature is "+str(max_temp)+"degrees.\n"+" Possible minimum temperature is "+str(min_temp)+"degrees.\n"+" The wind speed is at " + str(windspeed) + "meters per second.\n The humidity in air is "+ str(humidity)+"% \n"+" Overall it is " + str(description))

        elif "tell me a joke" in voice_input or "want to say something" in voice_input:
            rand=(pyjokes.get_joke())
            speak(rand)

        elif "what is your name" in voice_input or "whats your name" in voice_input or "your name please" in voice_input or "your name" in voice_input:
            speak("call me S.P.A.M sir")
            speak("Specially Programmed Artificial Memory")

        elif "thankyou" in voice_input or "thanks" in voice_input or "good job" in voice_input or "thank you soo much" in voice_input:
            randomtext=["hmmmmmmm","its ok sir","my pleasure sir","welcome sir","its my responsibility sir"]
            speak(random.choice(randomtext))

        elif "who is your creator" in voice_input or "who created you" in voice_input or "who made you" in voice_input:
            speak("Master Monish Kumar")

        elif "super user" in voice_input or "root" in voice_input or "super access" in voice_input or "administrator" in voice_input or "your master" in voice_input:
	    os.system('su')
            speak("Full Access Permission Granted")
            speak("Awaiting your confirmation!..Master Monish")

        elif  "*" in voice_input:
            randomtext=["Be Polite To An AI","Coward speaks those....","I cannot take those as inputs","Mind Your Words..."]
            speak(random.choice(randomtext))

        elif ".com" in voice_input:
            webbrowser.get('firefox').open('http://www.' + voice_input)
            speak("Opening :" + voice_input)

        elif "open calculator" in voice_input or "calculator" in voice_input or "cal c" in voice_input:
            os.system('gnome-calculator')
            speak("Opening Calculator Sir!")

        elif "open notepad" in voice_input or "notepad" in voice_input or "show notepad" in voice_input:
            os.system('gedit')
            speak("Opening Notepad Sir!")

        elif "task manager" in voice_input or "open task manager" in voice_input or "gods eye" in voice_input:
            os.system('ps -a')
            speak("Opening Task Manager Sir!")

        elif "camera" in voice_input or "open camera" in voice_input or "mirror" in voice_input or "show me" in voice_input:
            os.system('cheese')
            speak("Opening Camera App Sir!")

        elif "open command prompt" in voice_input or "command prompt" in voice_input or "command terminal" in voice_input or "terminal" in voice_input:
            os.system('gnome-terminal')
            speak("Opening Command Prompt Sir!")

        elif "open file explorer" in voice_input or "file explorer" in  voice_input or "file manager" in voice_input:
            os.system('nautilus')
            speak("Showing You File Manager Sir!")

        elif "clear" in voice_input or "clear screen" in voice_input or "wipe screen" in voice_input:
            randomtext=["Cleared sir","Wiped off","Done"]
            os.system('clear')
            speak(random.choice(randomtext))

        elif "kill my laptop" in voice_input:
            os.system('shutdown')
            speak("Shutting Down Processes")
            speak("Bye Sir!")


        elif "plus" in voice_input or "subtract" in voice_input or "minus" in voice_input or "multiply" in voice_input or "divide"in voice_input or "calculate" in voice_input or "do math for" in voice_input or "tell me the value for" in voice_input or "value for" in voice_input:
            res = client.query(voice_input)
            results = next(res.results).text
            speak("Got it Sir.")
            speak("Sir....According to my math")
            speak(results)

        elif "who is" in voice_input or "search about" in voice_input or "tell me about" in voice_input or "what is" in voice_input or "show me about" in voice_input or "interesting about" in voice_input or "show wikipedia about" in voice_input:
            results = wikipedia.summary(voice_input, sentences=10)
            speak("Got it Sir.")
            speak("WIKIPEDIA says : ")
            speak(results)
        '''
        elif 'news for today' in voice_input:
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")
                for news in news_list[:15]:
                    sofiaResponse(news.title.text.encode('utf-8'))
            except Exception as e:
                print(e)
        '''



if __name__ == "__main__":

    os.system('clear')
    wishInTime()

    try:
        assistant()

    except KeyboardInterrupt:
        speak("You Pressed Control + C Sir......Im Leaving..")
        sys.exit()

    


