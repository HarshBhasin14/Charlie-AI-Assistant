import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia as wiki
import webbrowser
from tkinter import *
import tkinter as tk
from PIL import Image
from playsound import playsound
from threading import Thread
import FrontendGUI
import datetime
import psutil
import os
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def input_command():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

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
    elif(h>=16 and h<24):
        speak("Good Evening Sir!")
        
        speak("System Booted Successfully")
        speak("Chaaarlie Online and Ready!")

def sleep():
    return None

def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\admin\OneDrive\Documents\Charlie Screenshots\Screenshot.jpeg')
    playsound(r'C:\Users\Computer Clinic\Downloads\windows_10_notify.mp3')

def Security():
        return None


a=1

if __name__ == "__main__":
    wish()
    while True:
        query = input_command().lower()
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
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open google' in query):
                speak("Opening sir!")
                url='google.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open gmail' in query):
                url='gmail.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open classroom' in query):
                url='classroom.google.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
        
            elif('open stack overflow' in query or 'open stackoverflow' in query):
                url='stackoverflow.com'
                speak('opening sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open whatsapp' in query):
                speak('opening sir!')
                url = 'web.whatsapp.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)
        
            elif('open Webmusic' in query or 'open web music ' in query):
                speak('opening sir!')
                url = 'mp3quack.com'
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open(url)

            elif('search youtube' in query or 'search on youtube' in query):
                speak('What should I search Sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                search = input_command().lower()
                webbrowser.get('chrome').open_new_tab('https://www.youtube.com/results?search_query='+search)

            elif('search on google' in query or 'search google' in query):
                speak('What do I search Sir!')
                search_google= input_command().lower()
                if(search_google == 'none'):
                    speak('Please Try Again Sir!')
                    
                elif(sr.Recognizer().energy_threshold >=300):
                    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                    webbrowser.get('chrome').open_new_tab('https://www.google.com/search?q='+search_google)
                        

            elif('open a website' in query or 'open website' in query or 'open a site' in query or 'open a site' in query):
                speak('Which website Sir!')
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                search_chrome= input_command().lower()
                webbrowser.get('chrome').open_new_tab(search_chrome+'.com')

            elif('open ms word' in query):
                speak('Opening Microsoft Word Sir!')
                path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk'
                os.startfile(path)
            
            elif('open ms excel' in query):
                speak('Opening Microsoft Excel Sir!')
                path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk'
                os.startfile(path)

            elif('open ms outlook' in query or 'open outlook' in query):
                speak('Opening Microsoft Outlook Sir!')
                path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Outlook 2007.lnk'
                os.startfile(path)

            elif('open ms powerpoint' in query or 'open powerpoint' in query):
                speak('Opening Microsoft Powerpoint Sir!')
                path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk'
                os.startfile(path)

            elif('open chrome' in query or 'google chrome' in query):
                speak('Opening Google Chrome Sir!')
                path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)

            elif('take screenshot' in query):
                screenshot()

            
            


                 #SYSTEM CONTROLS

            elif('go offline' in query or 'sleep' in query or 'Charlie hold' in query):
                speak("Chaarlie Going Offline!")
                a=0
                speak('Chaarlie Offline')

            elif('shutdown my system' in query or 'shutdown system' in query):
                speak("Are you Sure to Shutdown Your System!")
                answer= input_command().lower()
                if('yes' in answer):
                    os.system('shutdown /s /t l')
                elif('no' in answer):
                    speak('Okay Sir!')

            elif('logout my user' in query or 'logout user' in query):
                speak("Are you Sure to Log Out Your User!")
                answer= input_command().lower()
                if('yes' in answer):
                    os.system('shutdown -l')
                elif('no' in answer):
                    speak('Okay Sir!')

            elif('restart my system' in query or 'restart system' in query):
                speak("Are you Sure to Restart Your System!")
                answer = input_command().lower()
                if('yes' in answer):
                    os.system('shutdown /r /t l')
                elif('no' in answer):
                    speak('Okay Sir!')

            
        elif(a==0):
            print('Charlie is Offline')
            speak('Chaaarlie is Offline')
            sleep()
            if('wake up' in query):
                a=1
                speak('Chaarlie back Online')


            
            

            
            

            
