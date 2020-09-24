# Importing neccery modules..

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import requests
import time 
from googlesearch import search as scrh
import google
from plyer import notification
import random 
from res import *

# Interraction...

if __name__ == "__main__":
    
    wishme()
    while True:
        query = takeCommand().lower()
        try:
            if 'wikipedia' in query:
                speak("Searching in Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'hello jarvis' in query:
                while True:
                    hello_item = random.choice(hello_attri)
                    playsound('tudu.wav')
                    speak(hello_item)
                    break
            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com") 
                speak("Opening Stack overflow")
            elif 'rest'in query:
                speak('For what time I should rest please enter below..')
                # inp = takeCommand().lower()
                local_time = float(input("Enter duration of rest in minutes :"))
                local_time = local_time * 60
                exe_time = local_time / 60
                
                if local_time == 60.0 :
                    speak(f'taking rest for {local_time} seconds')
                elif local_time < 60.0 :
                    speak(f'taking rest for {local_time} seconds')
                elif local_time > 60.0:
                    speak(f'taking rest for {exe_time} minutes')
                time.sleep(local_time)
                speak("Awaked again..Awaked again")
            elif 'how are you' in query:
                speak('I\'am fine sir waht about you.. ') 
            elif 'good morning to mam' in query:
                speak('Good Morning Mam Nice to meet you..')
            elif 'i am also fine' in query:
                speak('Nice to hear that.. ')
            elif 'nice work' in query:
                speak('Thank you so much sir..')
            elif 'who are you' in query:
                speak('I am Jarvis, a python based assistant.')
            elif 'what can you do' in query:
                speak('I may help you in doing most of your stuff.. I can open various system applications. I can open websites on your command. I can set reminders , I can send emails for you. I may search in google and wikipedia for you. I can tell you the time and the current weather. Thank you ')
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("Opening Youtube")
            elif 'google search' in query:
                speak("What should I search..")
                query1 = takeCommand().lower()
                try :
                    print("Initializing..")
                    print('Searching in Google..')
                    speak('According to google')
                    speak("Here is what I found..")
                    for j in scrh(query1, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                except Exception as e:
                    print("Say that agian please..")
                    speak("Unknown error ouccered")                              
            elif 'you send email' in query:
                speak('yes i can')
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("Opening Google")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\91829\\Desktop\\Downloads\\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(# music_directory_path, songs[0]))
                speak("Playing Music")
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the current time is {strTime}")
            #elif 'open whatsapp' in query:
               # codepath = "C:\\Users\\91829\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
               # os.startfile(codepath)
               # speak("Opening Whatsapp")
            elif 'open vs code' in query:
                codepath = "path to vs code if you want.."
                os.startfile(codepath)
                speak("Opening VS code")
            elif 'hello to my friend' in query:
                speak("Hello one and all")
            elif 'what is the weather' in query:
                speak('Please tell the destination..')
                city = takeCommand().lower()
                url = api_address + city
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                speak(f"Its currently{format_add}in {city}")
            elif 'yourself'in query:
                speak("#The des. is up to you")
            elif "thanks" in query:
                speak("Oh..my pleasure")
            elif 'set reminder' in query:
                speak('What shall I remind you about?')
                title = takeCommand().lower()
                speak("For how many minutes? Please enter below :")
                local_time = float(input("Enter duration of timer in minutes :"))
                # local_time = int(takeCommand())
                local_time = local_time * 60
                exe_time = local_time / 60
                if local_time == 60.0 :
                    speak(f'Reminder set for {local_time} seconds')
                    time.sleep(local_time)
                    speak(f'Reminder over named {title}, setted for {local_time} seconds')
                    notification.notify(
                        title = title,
                        message ="Please see to your reminder",
                        app_icon = "clock.ico",
                        timeout = 10)
                elif local_time < 60.0:
                    speak(f'Reminder set for {local_time} seconds')
                    time.sleep(local_time)
                    speak(f'Reminder over named {title}, setted for {local_time} seconds')
                    notification.notify(
                        title = title,
                        message ="Please see to your reminder",
                        app_icon = "C:\\Users\\91829\\Desktop\\Main Prog\\Jarvis\\clock.ico",
                        timeout = 10)
                elif local_time > 60.0:
                    speak(f'Reminder set for {exe_time} minutes')
                    time.sleep(local_time)
                    speak(f'Reminder over named {title}, setted for {exe_time} minutes')
                    notification.notify(
                        title = title,
                        message ="Please see to your reminder",
                        app_icon = "clock.ico",
                        timeout = 10)
                              
            elif 'you scared me' in query:
                speak('Sorry..Sir for that..')    
                           
            elif 'send email' in query:
                while True:
                    try:
                        speak("whom you want to send the email..")
                        to = takeCommand().lower() #+ "@gmial.com" # Specifing if needed
                        # to = to.strip()
                        while True :
                            if to in dictid:
                                print(f'The required email id is {dictid[to]}') # First provide valid emails corresponding to name in samll letters in res.py file...
                                toE = dictid[to]
                                speak("What should I say to him?")
                                content = takeCommand()
                                sendEmail(toE, content)
                                speak("Sending E-mail")
                                speak("Email has been sent..!")
                                playsound('tudu.wav')
                                break
                            else:
                                speak("No such email id found..corresponding to name.")
                                playsound('error.wav')
                                break
                    except Exception as e:
                        print(e)
                        speak("Sorry! Sir... Email was not sent. Please try again")
                        playsound('replay.wav')
                    break
            elif 'exit' in query:
                speak("Thank You sir for your time..")
                playsound('off.wav')
                quit()
        except Exception as e:
            print(e)
            playsound('error.wav')
            speak('Unknown error occured.. ')
    
