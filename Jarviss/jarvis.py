import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import random
import pywhatkit
import pyjokes
import subprocess
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis Sir. Please tell me how may I help you")
def tellDay(): 
    day = datetime.datetime.today().weekday() + 1 
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week)

def tellTime(): 
    time = str(datetime.datetime.now())  
    print(time) 
    hour = time[11:13] 
    mn = time[14:16] 
    speak( "The time is sir" + hour + "Hours and" + mn + "Minutes")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Say that again please....')
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            time.sleep(3)    
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                time.sleep(5)        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
            time.sleep(5)     
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
            time.sleep(5)
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                time.sleep(5)    
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            time.sleep(5)    
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            time.sleep(5)
        elif 'play music' in query:
            music_dir = 'D:\\music_mp3'
            songs=os.listdir(music_dir)
            i=random.randint(0,120)
            os.startfile(os.path.join(music_dir,songs[i]))
            time.sleep(5)    
        elif 'the time' in query:
            tellTime();
            time.sleep(3)
        elif 'open chrome' in query:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            time.sleep(3)
        elif 'close chrome' in query:
            subprocess.call(["taskkill","/F","/IM","chrome.exe"])
            time.sleep(3)
        elif 'close music player' in query:
            subprocess.call(["taskkill","/F","/IM","Music.UI.exe"])
            time.sleep(3)
        elif 'close microsoft edge' in query:
            subprocess.call(["taskkill","/F","/IM","msedge.exe"])
            time.sleep(3)
        elif 'play' in query:
            speak('searching youtube...')
            query=query.replace("play","")
            pywhatkit.playonyt(query)
            time.sleep(5)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            time.sleep(3)   
        elif 'hey man' in query:
            speak("Hello Sir !")
            time.sleep(2)
        elif 'thank you' in query:
            speak("Anytime Sir!")
            time.sleep(2)
        elif 'how are you' in query:
            speak("I am fine Sir, Thank you")
            speak("How are you, Sir")
            time.sleep(2)
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            time.sleep(2)
        elif 'search' in query:
            query = query.replace("search", "")           
            webbrowser.open_new_tab(query)
            time.sleep(5) 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Pankaj")
            time.sleep(2) 
        elif "which day" in query: 
            tellDay()
            time.sleep(3) 
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India,Happy reading")
            time.sleep(5) 
        elif "exit" in query: 
            speak("Bye. Thank you Sir") 
            exit()
        
            
        
        

