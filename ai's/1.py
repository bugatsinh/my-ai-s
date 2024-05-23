import speech_recognition as sr
import openai
import wikipedia as wk
import os
import pyaudio
import pyttsx3


engin = pyttsx3.init("sapi5")
speaker=engin.getProperty('voices')
engin.setProperty('voice',speaker[0].id)

def speak(s):
    engin.say(s)
    engin.runAndWait()

if __name__ == "__main__":
