# Importing

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
import requests
import time 
from googlesearch import search as scrh
import google
from plyer import notification
import random 
from res import *

# creating API
api_address='' # Find an API by signing in openweather and then put that in this space..

# Sounds 
# wing = playsound('wing.wav')
# swoosh = playsound('swoosh.wav')
# point = playsound('point.wav')
# hit = playsound('hit.wav')
# die = playsound('die.wav')

# Hello random
hello_attri = ['yes sir', 'yes master', 'order master', 'hy master', 'what to do sir']


# generating engines
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Foe speaking
def speak(audio):
    '''
    This function helps assistance to speak and reply
    '''
    engine.say(audio)
    engine.runAndWait()

#  For wishing me..
def wishme():
    '''
    This function helps our assitance to wish us..
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print("Good Morning, Sir")
        speak("Good Morning, Sir")
    elif hour >=12 and hour <18:
        print("Good Afternoon, Sir")
        speak("Good Afternoon, Sir")
    else:
        print("Good Evening, Sir")
        speak("Good Evening, Sir")
    speak("I am Jarvis AI.. please tell me how may I help you.")

#  For taking commands
def takeCommand():
    '''
    It takes microphone input from the user and returns string output...
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.2
        r.non_speaking_duration = 0.2
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"                            User said, {query}\n")

    except Exception as e:
        # print(e) #If not recognized
        print("Say that again please..")
        return "None"
    return query

#  For sending E-mails
def sendEmail(to, content):
    '''
    This function helps to assist and send email..
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email same as above', to, content)
    server.close() 

dictid = { "Specify your name and email id corespondingly.."
    
}
