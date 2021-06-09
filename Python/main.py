from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
import random

Window.clearcolor = (0.05, 0.05, 0.05, 0.8)

import json




path = "dict.json"
with open("dict.json", "r",encoding='utf-8') as read_file:
    LIB = json.load(read_file)
AppManager = ScreenManager()

target_Words = []

for key, value in LIB.items():
    target_Words.append(key)



print(target_Words)

class Main(Screen):
        pass

class Option(Screen):
    def switch_theme(self,bg_color, fg_color):
        Window.clearcolor = bg_color
        for screen in AppManager.screens:
            self.set_color(screen,Label,fg_color)
        print(AppManager.screens[0].children[0].children[2].children)
    def set_color(self,item, type, color):
        print(f"{item.__class__}, {type}")
        if item.__class__ != type:
            if item.children != []:
                for child_items in item.children:
                    self.set_color(child_items, type, color)
            else:
                pass
        else: item.color = color

class LernScreen(Screen):
    word  = ''
    def restart(self):
        self.try_count, self.right_count, self.wrong_count = 0, 0, 0
        self.new_word()
        AppManager.current = "Lern"
    def check(self,word):
        self.try_count += 1
        if any(WORD == word.lower() for WORD in LIB[self.word]):
            self.right_count += 1
            self.new_word()
        else:
            self.wrong_count += 1
            self.wrong_word()
    def new_word(self):
        self.word = random.choice(target_Words)
        self.ids['WORD'].text = self.word
        self.ids['input'].text = ""
    def wrong_word(self):
        AppManager.get_screen('wrong').set_right_words(self.word)
        AppManager.current = "wrong"
        self.new_word()
    def finish_try(self):
        AppManager.get_screen('end').ids['try_count'].text = f'Всего попыток: {self.try_count}'
        AppManager.get_screen('end').ids['right_count'].text = f'Верных ответов: {self.right_count}'
        AppManager.get_screen('end').ids['wrong_coutn'].text = f'Неверных ответов: {self.wrong_count}'
        AppManager.current = "end"
        pass

class WrongScreen(Screen):
    def set_right_words(self, word):
        self.ids['right_words'].text = "Правельные варианты: " + ', '.join(LIB[word])
    pass

class EndScreen(Screen):
    pass



Builder.load_file("AppInterface.kv")

class AnyLang(App):
    def build(self):
        AppManager.add_widget(Main())
        AppManager.add_widget(Option())
        AppManager.add_widget(LernScreen())
        AppManager.add_widget(WrongScreen())
        AppManager.add_widget(EndScreen())
        AppManager.get_screen('Lern').new_word()
        return AppManager

if __name__ == "__main__":
    AnyLang().run()