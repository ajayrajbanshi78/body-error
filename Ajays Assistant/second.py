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


