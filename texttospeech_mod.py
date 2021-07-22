import pyaudio
import speech_recognition as sr
import gtts
from playsound import playsound
def texttospeech():
  # text_data = input("Type something")
  tts = gtts.gTTS(text_data)