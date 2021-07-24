import pyaudio
import speech_recognition as sr
import gtts
import pyttsx3
from playsound import playsound
engine = pyttsx3.init()
def texttospeech():
  engine = pyttsx3.init()
  text_data = input("Type something: ")
  engine.say(text_data)
  engine.runAndWait()
