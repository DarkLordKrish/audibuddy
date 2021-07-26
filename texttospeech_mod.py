import pyaudio
import speech_recognition as sr
import pyttsx3
from playsound import playsound
engine = pyttsx3.init()
def texttospeech(data):
  engine = pyttsx3.init()
  engine.say(data)
  engine.runAndWait()
