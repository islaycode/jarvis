import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good morning")
        speak("good morning")
    
    elif hour>=12 and hour <18:
        print("good afternoon")
        speak("Good afternoon")

    else:
        print("good evening")
        speak("Good evening")
    print("Hi my name is Jarvis, Please command me what to do?")     
    speak("Hi my name is Jarvis, Please command me what to do")        
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
          print('Listening...')
          r.pause_threshold= 0.6
          audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please Say that again ?")
        speak("Please say that again")
        return "None"
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dnikhil.dev@gmail.com', 'nikhil135')
    server.sendmail('dnikhil.dev@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()   
    while True:
   # if 1:

        query=takecommand().lower()
      #Logic for executing taks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
                speak("Ok sir opening yotube")
                webbrowser.open('www.youtube.com')

        elif 'google' in query:
                speak("Ok sir opening google")
                webbrowser.open("google.com")

        elif 'facebook' in query:
                speak("Ok sir opening Facebook")
                webbrowser.open("facebook.com")

        elif 'stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir The time is {strtime}")
            print(strtime)                      

        elif 'chrome' in query:
            speak("Ok sir opening google chrome")    
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'email to nikhil' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "dnikhil.dev@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry failed to send your email")   
        
        elif 'exit' in query:
            speak('Ok quitting jarvis have a good day')
            exit()
        
        elif 'bye' in query:
            speak('Bye have a good day')
            exit()    
            

        elif 'repeat' in query:
            speak(takecommand())         

        elif "hello" in query:
            print("hello, how are you ?")
            speak("hello how are you ?")
        
        elif 'how are you' in query:
            print("i'm good thank you for asking, how are you?")
            
            speak("i'm good thank you for asking, how are you?")

