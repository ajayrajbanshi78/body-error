import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime


#Initialize the recognition and text-to-speech engine 
listener = sr.Recognizer()
engine = pyttsx3.init()

#set female voice (opttional)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    #Convert text to speech
    print("alexa:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    #LIsten to user's voice and recognize the command 
    command = "hello alexa" 

    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = list.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.repalce("alexa","").strip()
                print("You said:",command)
    except sr.UnknownValueError:
        print("sorry, I didn't understant that")
    except sr.RequestError:
        print("Network error. Check your internet connection.")
    return command

def run_alexa():
    #process the command and response accordingly
    command = take_command()

    if 'play' in command: 
        song = command.replace('play', '').strip()
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datatime.datatime.now().strftime('%I: %M %P')
        talk ("The current time is " + time)

    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'data' in command:
        talk("sorry, I have a headache today .")
    
    elif 'are you single' in command:
        talk("I am in a relationship with WI-Fi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif command != "":
        talk("Please say the command again.")
    else:
        pass # No voice detected, ignore silently

#Run alexa continuosly
while True:
    run_alexa()
q