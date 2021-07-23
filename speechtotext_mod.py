
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

def Speechtotext():
  with sr.Microphone() as source:
  #    read audio from mic
    try:
      audio_data = r.listen(source,phrase_time_limit=5)
      print("Recognising......")
      text = r.recognize_google(audio_data)
      print(text)
    except:
      print("Sorry i couldnt recognise")
      

