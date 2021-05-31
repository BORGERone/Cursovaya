import os
import ast
import time

from kivy.properties import ObjectProperty
from kivy.config import ConfigParser
from kivy.factory import Factory

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class OptionWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class StWindow(Screen):
    pass
class St1(Screen):
    pass
class St2(Screen):
    pass
class St3(Screen):
    pass
class St4(Screen):
    pass
class St5(Screen):
    pass
class St6(Screen):
    pass
class St7(Screen):
    pass
class St8(Screen):
    pass
class St9(Screen):
    pass
class St10(Screen):
    pass
class StF(Screen):
    pass
class StF1(Screen):
    pass
class StF2(Screen):
    pass
class StF3(Screen):
    pass
class StF4(Screen):
    pass
class StF5(Screen):
    pass
class StF6(Screen):
    pass
class StF7(Screen):
    pass
class StF8(Screen):
    pass
class StF9(Screen):
    pass
class StF10(Screen):
    pass



kv = Builder.load_file('new_window.kv')




class AwesomeApp(App):
    def build(self):
        return  kv



if __name__ == '__main__':
    AwesomeApp().run()