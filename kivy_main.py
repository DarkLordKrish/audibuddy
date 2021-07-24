import speechtotext_mod
import texttospeech_mod
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Audibuddy(App):
    def build(self):
        return Label(text = "Does this work")
if __name__  ==  "__main__":
    Audibuddy().run()