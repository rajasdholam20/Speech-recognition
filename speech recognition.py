import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am sophia, Please tell me how can I help you")       


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Rajas...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing Rajas...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please Rajas...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajasdhdhd@gmail.com', 'fdsfsg')
    server.sendmail('rajassfdfsdf@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'hi sophia' in query:
            print("hi rajas")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/")  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to rajas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajassdfdsf@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rajas, I am not able to send this email")    
        else:
            print("No query matched")


        
