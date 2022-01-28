#This is by Tinnawut Noinarai
import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
import wikipedia
import pyjokes
import pyautogui as pg
import webbrowser
from time import ctime
import keyboard
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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command

def activate():
    try:
        with sr.Microphone() as source:
            print('activating....')
            talk('activating')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hi friday' or 'hey friday' or 'friday' in command:
                greetings = [f"hey, how can I help you my master", f"what's up master?",
                             f"I'm listening master", f"how can I help you master?",
                             f"hello master"]
                greet = greetings[random.randint(0, len(greetings) - 1)]
                print(greet)
                talk(greet)
                run_friday()
    except:
        pass
    return command


def run_friday():
    command = take_command()
    print('User:' + command)
    if 'play' in command:
        song = command.replace('can you play', '')
        talk('sure')
        talk('playing' + song )
        pywhatkit.playonyt(song)
        print(song)
    elif 'what time is it' in command:
        print(ctime())
        talk('okay, current time is ' + ctime())
    elif 'what is' in command:
        talk('there you go')
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am very well, thanks for asking my master')
        print('I am very well, thanks for asking my master')
    elif 'how are you doing' in command:
        talk('all good thank you for asking my master')
        print('all good thank you for asking my master')
    elif 'joke' in command:
        talk('sure' + pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'search' in command:
        topic = command.replace('can you search', '')
        talk('sure, here is what I found for'+ topic)
        pywhatkit.search(topic)
    elif 'goodbye' in command:
        talk('see you later master')
    elif 'nothing now' in command:
        talk('okay if you want something later be my guest')
        print('okay if you want something later be my guest')
    elif 'screenshot' in command:
        im1 = pg.screenshot()
        im1.save('my_screenshot.png')
        talk('done master')
        print('done master')
    elif 'thailand' in command:
        webbrowser.open_new_tab('https://meet.google.com/vbu-dnkc-xwu?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'basic math' in command:
        webbrowser.open_new_tab('https://meet.google.com/dgz-omjm-tco?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'chemistry' in command:
        webbrowser.open_new_tab('https://meet.google.com/exx-ziie-sug?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'english' in command:
        webbrowser.open_new_tab('https://meet.google.com/fnj-khib-vac?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'reading' in command:
        webbrowser.open_new_tab('https://meet.google.com/ahc-ocsh-tfu?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'biology' in command:
        webbrowser.open_new_tab('https://meet.google.com/oxg-syrv-udt?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'southeast asia' in command:
        webbrowser.open_new_tab('https://meet.google.com/xmh-zcwe-shp?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'not basic math' in command:
        webbrowser.open_new_tab('https://meet.google.com/bsjjtkpxrm?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'social' in command:
        webbrowser.open_new_tab('https://meet.google.com/kpa-pfxz-xds?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'health' in command:
        webbrowser.open_new_tab('https://meet.google.com/epm-ozsd-pkj?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'entertain' in command:
        webbrowser.open_new_tab('https://meet.google.com/wqu-fxrv-wyh?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'boring' in command:
        webbrowser.open_new_tab('https://meet.google.com/ibm-upze-fyq?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'technology' in command:
        webbrowser.open_new_tab('https://meet.google.com/zkh-nazj-idt?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'creation' in command:
        webbrowser.open_new_tab('https://meet.google.com/vyq-wjoq-iyq?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'admission' in command:
        webbrowser.open_new_tab('https://meet.google.com/lookup/hdc7gy3hko?authuser=0&hs=179')
        pg.countdown(7)
        pg.click(1202, 647)
        keyboard.press_and_release('ctrl+d')
        keyboard.press_and_release('ctrl+e')
        pg.countdown(3)
        pg.click(1338, 586)
    elif 'let me out' in command:
        pg.countdown(1)
        pg.click(1120, 968)
    else:
        talk('I do not understand what are you saying')
        run_friday()

activate()






