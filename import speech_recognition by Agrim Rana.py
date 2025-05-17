import speech_recognition as sr
import pyttsx3  #text to speech
import datetime
import wikipedia 
import pywhatkit #yt 

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning!")
    elif 12 <= hour < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("I Am Agrim's AI assistant. How can I help you?")

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except:
        return ""

def run_assistant():
    wish_user()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            talk("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            result = wikipedia.summary(topic, sentences=2)
            print(result)
            talk(result)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"Current time is {time}")

        elif 'play' in command:
            song = command.replace('play', '')
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'stop' in command or 'exit' in command:
            talk("Goodbye!")
            break

        elif command == "":
            talk("Sorry, I didn’t catch that. Please try again.")

        else:
            talk("I didn’t understand. Please say it again.")

run_assistant()
