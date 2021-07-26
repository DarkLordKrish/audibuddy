import pyaudio
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

    
        

    
class Audibuddy(App):
    def build(self):
        return FloatLayout()
if __name__  ==  "__main__":
    Audibuddy().run()