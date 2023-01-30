# thats my dependecies
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# don't forget to follow my github
print('===========[ZETA]==========')
print('follow github.com/veldanava')
print('========[ASSISTANT]========')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.5)
# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

# Takes Input from User
def take_user_input():
    r = sr.Recognizer()
    # print("audio source list", sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print("You said : {}".format(text))
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 20 and hour < 6:
                speak("Good night oniisan, take care!")
            else:
                speak('Have a good day oniisan!')
            exit()
    except Exception:
        speak('Sorry, I could not understand oniisan. Could you please say that again?')
        query = 'None'
    return query

# main function
if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        # open notepad
        if 'notepad' in query:
            open_notepad()
        # open discord
        elif 'open discord' in query:
            open_discord()
        # open cmd
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        # open camera
        elif 'open camera' in query:
            open_camera()
        # open calculator
        elif 'open calculator' in query:
            open_calculator()
        # find my ip
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen oniisan.')
            print(f'Your IP Address is {ip_address}')
        # wikipedia search
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, oniisan?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen oniisan.")
            print(results)
        # open youtube
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, oniisan?')
            video = take_user_input().lower()
            play_on_youtube(video)
        # google seacrh
        elif 'google' in query:
            speak('What do you want to search on Google, oniisan?')
            query = take_user_input().lower()
            search_on_google(query)
        # send whatsapp message
        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message oniisan? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message oniisan?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message oniisan.")
        # send email
        elif "email" in query:
            speak("On what email address do I send oniisan? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject oniisan?")
            subject = take_user_input().capitalize()
            speak("What is the message oniisan?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email oniisan.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs oniisan.")
        # gimme a joke XD
        elif 'joke' in query:
            speak(f"Hope you like this one oniisan")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen oniisan.")
            pprint(joke)
        # gimme a advice
        elif "advice" in query:
            speak(f"Here's an advice for you, oniisan")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen oniisan.")
            pprint(advice)
        # get a trending movies
        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen oniisan.")
            print(*get_trending_movies(), sep='\n')
        # get a trending news
        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, oniisan")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen oniisan.")
            print(*get_latest_news(), sep='\n')
        # get weather today
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen oniisan.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")