from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
import random

path = "DICT.TXT"
parsedLIB = open(path).read().split("\n")

LIB = {}
for i in range(int(len(parsedLIB)/2)):
    LIB.setdefault(parsedLIB[i], parsedLIB[i+1].split("\t"))

class Main(Screen):
    pass
class LernScreen(Screen):
    word = "a little"
    def check(self,word):
        if any(elements in word for elements in LIB[self.word]):
            self.new_word()
        else:
            self.wrong_word()
        print(LIB[self.word])
    def new_word(self):
        self.word = random.choice(list(LIB.keys()))
        self.ids["WORD"].text = self.word
        self.ids["input"].text = ""
    def wrong_word(self):
        print('non lol')
    pass
class WrongScreen(Screen):
    right_word = ""


Builder.load_file("AppInterface.kv")

class AniLang(App):
    AppManager = ScreenManager()
    def build(self):
        self.AppManager.add_widget(Main())
        self.AppManager.add_widget(LernScreen())
        return self.AppManager

if __name__ == "__main__":
    AniLang().run()