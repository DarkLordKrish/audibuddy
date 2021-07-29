import pyaudio
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.toast import toast




r = sr.Recognizer()
mic  = sr.Microphone()


class MainWindow(Screen):
    LabelBase.register(name='Roboto-Thin', 
                   fn_regular='Roboto-Thin.ttf')
    def exit(self):
        quit()
        
class speechtotext(Screen):
    r = sr.Recognizer()
    LabelBase.register(name='Roboto-Thin', 
                   fn_regular='Roboto-Thin.ttf')
    
    def record(self):
        global audio_data
        
        with mic as source:
            
            
            
            self.ids.final_text.text = "Recognizing...." 
            
            audio_data = r.record(source,duration = 5)
                
                
            
           
    def recognize(self,audio_data):
        try:
            recorded_text = r.recognize_google(audio_data)
            
        except sr.UnknownValueError:
            self.ids.final_text.text = "Sorry,I couldn't understand, please try again."
        except sr.RequestError:
            self.ids.final_text.text = 'Sorry, the service is down'
        self.ids.final_text.text = recorded_text
    def final(self):
        self.recognize(audio_data)
        
    def exit(self):
        quit()
    
            
            
    
class texttospeech(Screen):
    engine = pyttsx3.init()
    LabelBase.register(name='Roboto-Thin', 
                   fn_regular='Roboto-Thin.ttf')
    def exit(self):
        quit()
    def texttospeechfas(self):
        self.engine.say(self.ids.text.text)
        self.engine.runAndWait()
class aboutus(Screen):
     LabelBase.register(name='Roboto-Thin', 
                   fn_regular='Roboto-Thin.ttf')
     def exit(self):
        quit()
class WindowManager(ScreenManager):
    def exit(self):
        quit()
kv = Builder.load_file("main.kv")



class Audibuddy(App):
    
    def build(self):
        return kv
if __name__  ==  "__main__":
    Audibuddy().run()