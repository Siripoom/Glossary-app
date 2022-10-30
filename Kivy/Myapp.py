from cProfile import label
from os import kill


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MygridLayout(GridLayout):
    


class Myapp(App):
    def build(self):
        return Label(text="Hello world")

Myapp().run()