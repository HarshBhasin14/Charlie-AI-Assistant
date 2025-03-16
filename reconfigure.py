import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        a.pause_threshold = 1
        audio = a.listen(source)

    try:
        print('Recognizing....')
        query = a.recognize_google(audio, language='en=in')
        print(f"User Said: {query}\n")
        

    except Exception as e:
        print("Please Say that again Sir....!")
        return "None"
    return query


if __name__=="__main__":
    speak('Charlie online and ready sir')
    take_command()

    