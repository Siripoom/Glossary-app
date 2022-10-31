from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import helpers
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen


class RegisterScreen(MDApp,Screen):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        
        username = Builder.load_string(helpers.Register_username_input)
        password = Builder.load_string(helpers.Register_password_input)
        phonenumber = Builder.load_string(helpers.Register_phone_input)
        button_signup = Builder.load_string(helpers.Register_button_Signup)
        

        screen.add_widget(username)
        screen.add_widget(password)
        screen.add_widget(button_signup)
        screen.add_widget(phonenumber)

        return screen
sm = ScreenManager()
#sm.add_widget(RegisterScreen(name='menu'))

class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        
        username = Builder.load_string(helpers.username_input)
        password = Builder.load_string(helpers.password_input)
        button_login = Builder.load_string(helpers.button_login)
        button_signup = Builder.load_string(helpers.button_Signup)
        #screen = Builder.load_string(helpers.screen_helper)

        screen.add_widget(username)
        screen.add_widget(password)
        screen.add_widget(button_login)
        screen.add_widget(button_signup)
        
        #return screen

RegisterScreen().run()
