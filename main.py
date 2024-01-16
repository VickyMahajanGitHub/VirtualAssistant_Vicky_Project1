import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import subprocess
import sys
import cv2
import time




def talk(text):

    # engine.say('Hi, I am Cadd your Virtual Assistant')
    # engine.say('What can I do for you')
    engine.say(text)
    engine.runAndWait()


def take_picture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("captured_image.jpg", frame)
    cap.release()
    talk("Picture taken and saved as captured_image.jpg")

def open_image():
    os.system('start captured_image.jpg')
    talk("Opening the captured image.")


def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 17:
        return "Afternoon"
    elif 17 <= current_hour < 20:
        return "Evening"
    else:
        return "Night"
def get_user_name():
    return "Vicky"

def welcome_message():
    user_name=get_user_name()
    time_of_day=get_time_of_day()
    greeting=f" Good,{time_of_day}, {user_name}, I am Cadd, Your Virtual assistant. How I can assist you today?"
    talk(greeting)
    print(greeting)






listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)





def givenews():

    apiKey = '49e391e7066c4158937096fb5e55fb5d'

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"

    r = requests.get(url)

    data = r.json()

    data = data["articles"]

    flag = True

    count = 0

    for items in data:

        count += 1

        if count > 5:

            break

        print(items["title"])

        to_speak = items["title"].split(" - ")[0]

        if flag:

            talk("Today's top five Headline are : ")

            flag = False

        else:

            talk("Next news :")

        talk(to_speak)

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f"You said: {query}\n")



    except Exception as e:

        print("Say that again please...")

        return "None"

    return query
    # try:
    #     with sr.Microphone() as source:
    #         print('listening....')
    #         voice = listener.listen(source)
    #         command = listener.recognize_google(voice)
    #         command = command.lower()
    #         if 'cadd' in command:
    #             command = command.replace('cadd', '')
    #             #talk(command)
    #             print(command)
    #       #  print(command)
    # except:
    #     pass
    # return command



def run_Cadd():
    command = take_command()
    print(f"User Command: {command}")  # Print the recognized command
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
       # print(song)

    elif 'wikipedia' in command.lower() or 'on wikipedia' in command.lower():
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    #



    # elif 'wikipedia' in command:
    #
    #     talk('Searching..')
    #
    #     query = command.replace("wikipedia", "")
    #
    #     results = wikipedia.summary(query, sentences=2)
    #
    #     talk("According to Wikipedia")
    #
    #     print(results)
    #
    #     talk(results)

    elif 'take a picture' in command.lower():
        take_picture()

    elif 'open image' in command.lower() or 'view image' in command.lower():
        open_image()



    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who is your creator' in command:
        talk('Vicky is my creator')
    elif 'joke' in command:

        j= talk(pyjokes.get_joke())
        print(j)

    elif 'temperature' in command:
        weather="temperature in Noida"
        url=f"https://www.google.com/search?q={weather}"
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temp=data.find("div", class_="BNeawe").text
        talk(f"current {weather} is {temp}")

    # elif 'youtube' in command:
    #     webbrowser.open("https://www.youtube.com")
    elif 'youtube' in command.lower() or 'open youtube' in command.lower():
        webbrowser.open("https://www.youtube.com")


    elif 'open browser' in command or 'open Google' in command:
        webbrowser.open("https://www.google.com")

    # elif 'open gmail' in command:
    #     webbrowser.open("https://mail.google.com")

    elif 'gmail' in command.lower() or 'open gmail' in command.lower():
        webbrowser.open("https://mail.google.com")


    elif 'command prompt' in command.lower() or 'open command prompt' in command.lower():
        os.system('start cmd')

    elif 'notepad' in command.lower() or 'open notepad' in command.lower():
        os.system('start notepad')

    elif 'whatsapp' in command:
        os.system('start whatsapp')

    # elif 'set alarm' in command:
    #     set_alarm()  # Call the new set_alarm function

    elif 'search' in command:
        # Extract the search query from the command
        query = command.replace('search', '').strip()
        search_url = f"https://www.google.com/search?q={query}"

        # Open the default web browser with the Google search URL
        webbrowser.open(search_url)

        talk(f"Here are the search results for {query} on Google.")

    elif 'onenote' in command or 'open onenote' in command:
        # Open Microsoft Mail(Outlook) based on the operating system
        if 'win' in sys.platform:  # this for Windows system only
            subprocess.run(["C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"])


    elif "calculator" in command:
        os.startfile(r"C:\Windows\System32\calc.exe")

    elif 'news' in command.lower() or ' today headlines' in command.lower():

        givenews()

    elif "open camera" in command:
        talk("Opening the camera...")
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('Camera Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()





    elif 'stop' in command or 'exit' in command:
        talk('Thanks for using me, have a good day')
        exit()
    else:
        talk('Sir do you have any other work')



# def open_whatsapp():
#     if 'win' in sys.platform:
#         subprocess.run([])



# def set_alarm():
#     talk("Sure, please specify the time for the alarm.")
#     try:
#         with sr.Microphone() as source:
#             print('listening for alarm time....')
#             voice = listener.listen(source)
#             alarm_time = listener.recognize_google(voice)
#             alarm_time = alarm_time.lower()
#
#         # Convert the spoken time to a datetime object
#         alarm_time_obj = datetime.datetime.strptime(alarm_time, '%I:%M %p')
#
#         # Get the current time
#         current_time = datetime.datetime.now()
#
#         # Calculate the time difference for the alarm
#         time_difference = (alarm_time_obj - current_time).total_seconds()
#
#         # Check if the alarm time is in the future
#         if time_difference > 0:
#             talk(f"Setting the alarm for {alarm_time}")
#             time.sleep(time_difference)
#             talk("Wake up! It's time!")
#
#         else:
#             talk("I'm sorry, but that time has already passed. Please provide a future time.")
#
#     except Exception as e:
#         print(e)
#         talk("Sorry, I couldn't understand the time. Please try again.")


# Call the welcome_message function before entering the loop
welcome_message()

while True:
    run_Cadd()




    # Upcoming Feature to be add
    # Basic Arithmatic Operation
    # To make to-do list
    # Set Alarm
    # Weather Information of any location in world
    # Send Email etc...
    # Search Any Place in the world.
