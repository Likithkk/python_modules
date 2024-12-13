import speech_recognition as sr
import pyttsx3
import wikipedia

#intiate an engine to convert text to speech
engine = pyttsx3.init()
voices=engine.getProperty('voices')
#1 is for female voice, 0 for male voice
engine.setProperty('voice',voices[1].id)
#for recognition
recognizer=sr.Recognizer()

with sr.Microphone() as source:
    #to clear background noises
    recognizer.adjust_for_ambient_noise(source,duration=0.5)
    #for input
    recordedaudio=recognizer.listen(source)
try:
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print("Message is "+format(text))    
except Exception as ex:
    print(ex)

wikisearch = wikipedia.summary(text)
engine.say(wikisearch)
engine.runAndWait()