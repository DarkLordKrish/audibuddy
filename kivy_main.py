# import speechtotext_mod
# import texttospeech_mod
import pyaudio
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
class MyGrid(GridLayout):
    engine = pyttsx3.init()
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.rows = 3
        self.rows = 1
        self.inside.add_widget(Label(text="Type your text: "))
        self.name = TextInput()
        self.inside.add_widget(self.name)
        self.convert = Button(text = "Convert to speech")
        self.convert.bind(on_press = self.Texttospeech)
        self.inside.add_widget(self.convert)
        self.add_widget(self.inside)
    def Texttospeech(self,instance):
        name = self.name.text
        self.engine.say(name)
        self.engine.runAndWait()
        print(name)
        self.name.text = ""
        
        
    
        

    
    
class Audibuddy(App):
    def build(self):
        return MyGrid()
if __name__  ==  "__main__":
    Audibuddy().run()