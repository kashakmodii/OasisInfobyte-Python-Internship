import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the results for {query}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
speak("Voice Assistant is ready.")
while True:
    command = listen()
    handle_command(command)
