import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
from tkinter import *
import tkinter as tk
from PIL import Image
from playsound import playsound
from threading import Thread
import FrontendGUI
import pywhatkit
import datetime

engine = pyttsx3.init()
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))

def speak(audio):          #Speak Function
    engine.say(audio)
    engine.runAndWait()
def wish():
    h= int(datetime.datetime.now().hour)
    if(h>=0 and h<12):
        speak("Good Morning Sir!")
        
        speak("System Booted Successfully")
        speak("Chaaarlie Online and Ready!")
    elif(h>=12 and h<16):
        speak("Good Afternoon Sir!")
        
        speak("System Booted Successfully")
        speak("Chaaarlie Online and Ready!")
    elif(h>16 and h<24):
        speak("Good Evening Sir!")
        
        speak("System Booted Successfully")
        speak("Chaaarlie Online and Ready!")

def input_command():           #Input from Microphone and return string Output
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        a.pause_threshold = 0.8
        audio = a.listen(source)     #Reference to speak function
    try:
        print("Processing....")
        query =a.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Please Say Again Sir!") 
        return "None"
    return query

    def Frontend():
        return FrontendGUI
def sleep():
    return None
a=1
if (__name__== "__main__"):
    wish()
    while True:
        query=input_command().lower() #Execution
        if(a==1):
            if 'wikipedia' in query:
                speak("Searching Wikipedia sir!")
                query=query.replace("wikipedia", "")
                results = wiki.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif('open youtube' in query):
                speak('opening sir!')
                url = 'youtube.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open google' in query):
                speak("Opening sir!")
                url='google.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open gmail' in query):
                url='gmail.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open classroom' in query):
                url='classroom.google.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open stack overflow' in query or 'open stackoverflow' in query):
                url='stackoverflow.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open whatsapp' in query):
                speak('opening sir!')
                url = 'web.whatsapp.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open Webmusic' in query or 'open web music ' in query):
                speak('opening sir!')
                url = 'mp3quack.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)

            elif('search youtube' in query or 'search on youtube' in query):
                speak('What should I search Sir!')
                search = input_command().lower()
                webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+search)

            elif('search on google' in query or 'search google' in query):
                speak('What do I search Sir!')
                search_google= input_command().lower()
                webbrowser.open_new_tab(search_google)

            elif('search on chrome' in query or 'search chrome' in query):
                speak('What do I search Sir!')
                search_chrome= input_command().lower()
                webbrowser.open_new_tab(search_chrome+'.com')


                 #SYSTEM CONTROLS

            elif('go offline' in query or 'sleep' in query or 'hold' in query):
                speak("Chaarlie Going Offline!")
                a=0
                speak('Chaarlie Offline')
            
            

            
            
        elif(a==0):
            print('Charlie is Offline')
            sleep()
            if('wake up' in query):
                a=1
                speak('Chaarlie back Online')

        
       
        
        
        
         
        
        
            

            




        


