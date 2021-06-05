import datetime
import speech_recognition as sr   #( install speechRecognition module)
import pyttsx3              #install pyttsx3 module
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning dear!")
    elif hour>= 12 and hour<18:
        speak("Good afternoon dear!")
    else:
        speak("Good evening dear!")

    speak("I am your personal virtual assistant, Sara, How may I help you ?  ")

def takeCommand():
    #takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that Again Please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while(True):
        query = takeCommand().lower()

        #Tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences= 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time please' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'open chrome' in query:
            chrome ="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome)

        elif 'shutdown' in query:
            speak('Assistant software shut down initiated')
            speak('5, 4, 3, 2, 1, 0 ')
            exit()






