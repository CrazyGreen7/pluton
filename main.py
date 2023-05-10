import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import time
import wolframalpha
import json
import requests
from datetime import datetime
import openai
from textblob import TextBlob
from bs4 import BeautifulSoup 
import snakegame
import pygame
import time
import random
import smtplib
import sys
import numpy as np

openai.api_key = "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"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 3)

def speak(text):
   engine.say(text)
   engine.runAndWait()


def greet():
   hour = datetime.now().hour
   if hour >= 0 and hour < 12:
       speak("Good morning!")
   elif hour >= 12 and hour < 18:
       speak("Good afternoon!")
   else:
       speak("Good evening!")
def send_email(to, subject, message):
   server = smtplib.SMTP('smtp.gmail.com', )
   server.ehlo()
   server.starttls()
   email = "plutonbeta0.1@gmail.com"
   password = "Pluton@beta_0.1"
   server.login(email, password)
   email_message = f'Subject: {subject}\n\n{message}'
   server.sendmail(email, to, email_message)
   server.quit()


def recognize_speech():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       r.adjust_for_ambient_noise(source)
       audio = r.listen(source)
       try:
           statement = r.recognize_google(audio, language='en-gb')
           print(f"You said: {statement}\n")
       except Exception as e:
           print(e)
           speak("I didn't hear you, please say that again")
           return "none"
       return statement.lower()

def delete_elements(list, a, b, c):
   del list[a]
   del list[b]
   del list[c]

def speak1():
   print("This is artificial intelligence Pluton speaking to you. ")
   speak("Hi , this is artificial intelligence Pluton speaking to you.")



print("Loading Pluton beta 0.1")
speak("Loading Pluton beta 0.1")
greet()

while True:
   try:
       speak("What can I do for you?")
       statement = recognize_speech()

       if statement == "none":
           continue


       blob = TextBlob(statement)
       polarity = blob.sentiment.polarity

       if polarity > 0.5:
           speak("That sounds great!")
       elif polarity < -0.5:
           speak("I'm sorry to hear that.")
       else:
           speak("Hmm, interesting.")

       if "goodbye" in statement or "bye" in statement or "turn off" in statement:
           speak('See you later!')
           break

      

       elif 'open youtube' in statement:
           webbrowser.open_new_tab("https://youtube.com")
           speak("YouTube is now open")
           time.sleep(3)


       elif 'google' in statement:
           webbrowser.open_new_tab("https://www.google.com")


       elif "hai" in statement or "hello" in statement or "hi" in statement or "hey" in statement:
           speak1()


       elif "what's the time" in statement or "time" in statement or "what is the time " in statement:
           currentTime = datetime.now().strftime("%I:%M %p")
           print("The current time is", currentTime)
           speak("The current time is " + currentTime)

       elif "image" in statement or "picture" in statement or "photo" in statement:
           sentence = statement.split()
           keyword = sentence[-1]
           webbrowser.open_new_tab("https://unsplash.com/s/photos/" + keyword)
           speak("Please select image of your choice")

       elif "search" in statement and "youtube" in statement:
           sentence = statement.split()
           delete_elements(sentence, 0, -1, -1)
           link = "https://www.youtube.com/results?search_query="
           for word in sentence:
               link = link + word + "+"
           webbrowser.open_new_tab(link)

       elif "games" in statement or "game" in statement or "fun" in statement:
           speak("what games would you like to play? the options are: chess, snakegame,tic tac toe")
           game_name= recognize_speech()
           if "chess" in game_name:
               webbrowser.open_new_tab("chess.com")
           elif "snake" in game_name or "snakegame" in game_name:
               snakegame.playsnakegame()
               continue
           elif "tick" in game_name or "tic"  in game_name or "tack" in game_name or "tac" in game_name:
               
               continue
           elif "ping" in game_name or "pong" in game_name:
               snakegame.playpingpong()
               
            #test
           elif game_name == "none":
                continue
       elif "send a email" in statement or "email" in statement or "mail" in statement:
            speak("Enter the recipient's address")
            remail = input("Enter the recipient's address : ")
            speak("Enter the subject")
            sub = input("Enter the subject :")
            speak("Do you want to say the message or type the message")
            print("Do you want to say to the message or type the message")
            option=recognize_speech()

            if "say" or "speak" in option :
                print("Listening.....")
                speak("Listening.....")
                message = recognize_speech()
                send_email(remail, sub, message)
                speak("Email sent!")
                print("Email sent!")
            elif "type" in option:
                typemessage = input("Enter the message :")
                speak("Enter the message")
                send_email(remail, sub, typemessage)
                speak("Email sent!")
                print("Email sent!")
            else:
                continue
       
       elif "why" in statement or "when" in statement or "what" in statement or "how" in statement or "define" in statement or "which" in statement or "who" in statement:
            statement = statement.replace("wikipedia", "")
            try:
                results = wikipedia.summary(statement, sentences=3)
                speak(results)
            except wikipedia.exceptions.PageError as e:
                print(e)
                speak("Sorry, I could not find any results")
            except wikipedia.exceptions.DisambiguationError as e:
                print(e)
                speak(f"Can you please clarify which {statement} you are referring to?")

   except Exception as e:
       print(e)
       speak("Sorry, something went wrong. Please try again.")