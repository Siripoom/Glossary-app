from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import helpers
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200)
        username = Builder.load_string(helpers.username_input)
        password = Builder.load_string(helpers.password_input)

        button_login = Builder.load_string(helpers.button_login)
        button_signup = Builder.load_string(helpers.button_Signup)
        screen.add_widget(username)
        screen.add_widget(password)
        screen.add_widget(button_login)
        screen.add_widget(button_signup)
        return screen

App().run()
