import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('yes master')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
    except:
        pass
    return command


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with your wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'apurv' in command:
        talk ('He is your friend and he is in relationship with ashish also known as anni')
    elif 'arpita' in command:
        talk('she is a nepali and someone whose parent had a great new year evening ')
    elif 'ashish' in command:
        talk('friends of yours and a baniya.')
    elif 'uncle' in command:
        talk('uncle is a milk vendor')
    elif 'kartik' in command:
        talk('one who is always ready to poke professors.')
    elif 'aditya' in command:
        talk('he is the yogi of the class')
    elif 'dev' in command:
        talk('he is my master and above all , respect him if he is with you.')
    elif 'shanu' in command:
        talk('she is a mom of a handsome boy.')
    elif 'akash' in command:
        talk('he is your brother.')
    elif 'chandan' in command:
        talk("a true friend of your's ." )
    else:
        talk('Please say the command again.')


while True:
  run_friday()