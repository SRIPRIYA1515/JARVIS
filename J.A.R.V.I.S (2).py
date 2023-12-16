import serial
import random
import datetime
import googlesearch
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        a = "Good morning Tharun", "Good morning sir", "Hello Tharun Good Morning", "O, Good morning sir", "O, good morning Tharun", "Wow! Welcome back Tharun sir"
        speak(random.choice(a))
    elif hour >= 12 and hour < 18:
        b = "Good Afternoon Tharun", "Good Afternoon sir", "Hello Tharun Good Afternoon", "O, Good Afternoon sir", "O, good Afternoon Tharun", "Wow! Welcome back Tharun sir"
        speak(random.choice(b))
    else:

        c = "Good Evening Tharun", "Good Evening sir", "Hello Tharun Good Evening", "O, Good Evening sir", "O, good Evening Tharun", "Wow! Welcome back Tharun sir"
        speak(random.choice(c))


wishMe()
wel = "So, how can i help you sir!", "How can i help", "Give me a command Sir", "Online and ready sir", "What can i do for you sir", "Please give me a command Sir"
speak(random.choice(wel))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("....")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences=2)

                speak("so, wikipedia says")
                speak(results)

            except:
                speak("Not available on wikipedia")

        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            break
        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")


        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query or 'web browser' in query:
            ak = "what should i search?", "please say the words you want to search for", "what would you like to search sir?", "I am typing, say what you want to search on google?"
            speak(random.choice(ak))
            h = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={h}")

            #webbrowser.open("www.google.com")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")


        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:

                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")
        elif 'who are you' in query or "give me your introduction" in query:
            speak(
                "Wait, i am introducing myself. My name is Jarvis, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human", "You are Tharun", "You are a human", "I cant identify peoples with their vocies, may be you are Tharun or anybody with relation of Tharun"
            speak(random.choice(jh))
        elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))
        elif 'what is your name' in query:
            speak("My name is JARVIS sir.")
            speak("I am your Personal Assistant.")
        elif "jarvis" in query:
            speak("Yes It is me")
            speak("Is there any work to be done??")
        elif "what is" in query or "who is" in query or "when is" in query or "where is" in query or "how is" in query or "when was" in query:
            query = query.replace("What is","")
            speak("Hey, Look this is what I found from Google...")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "tell me the time now" in query:
            curr = time.time()
            curr_time = time.ctime(curr)
            speak(curr_time)
            print()
        elif "play some music" in query or "hit some music" in query or "music" in query:
            speak("Which type of music do you want, such as...")
            speak("Romantic")
            speak("Party types...")
            speak("Rap??")
            r = takeCommand().lower()
            if r == "romantic":
                speak("Ok sir playing your favorite romantic playist...")
                webbrowser.open(f"https://music.youtube.com/watch?v=4z-oDk1utVo&list=RDAMVM4z-oDk1utVo{query}")
            elif r == "happy songs":
                speak("Ok sir I will make sure to set fire on the stage...")
                webbrowser.open(f"https://music.youtube.com/watch?v=5c3a9A0A1pg&list=RDAMVM5c3a9A0A1pg{query}")
            elif r == "rap":
                speak("Whose rap do you want listen??")
                speak("Emiway??")
                speak("or")
                speak("Boolywood raps??")
                speak("or")
                speak("Gully boy movie songs??")
                h = takeCommand().lower()
                if h == "emiway":
                    speak("Playing Emiway Bantai Raps...")
                    webbrowser.open(f"https://music.youtube.com/watch?v=5c3a9A0A1pg&list=RDAMVM5c3a9A0A1pg{query}")
                speak("Ok sir Your favorite raps are here...")
                webbrowser.open(f"https://music.youtube.com/watch?v=5c3a9A0A1pg&list=RDAMVM5c3a9A0A1pg{query}")
        elif "turn on the light" in query:
