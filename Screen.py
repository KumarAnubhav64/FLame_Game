# Flames App made on kivy framework by Kumar Anubhav

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (360, 700)
# define our differnt screen


class FirstWindow(Screen):
    def FlameLogic(self):
        him_name = self.ids.Him.text
        her_name = self.ids.Her.text
        self.ids.Button_Image.source = 'images/Button_pressed.png'
        uncommon_char = []
        for i in him_name:
            if i not in her_name:
                uncommon_char.append(i)
        for i in her_name:
            if i not in him_name:
                uncommon_char.append(i)
        flame = len(uncommon_char)
        pos_flame = flame % 5
        if pos_flame == 0:
            self.ids.Match.source = 'images/Friend.png'
        elif pos_flame == 1:
            self.ids.Match.source = 'images/love.png'
        elif pos_flame == 2:
            self.ids.Match.source = 'images/Affection.png'
        elif pos_flame == 3:
            self.ids.Match.source = 'images/mar.png'
        elif pos_flame == 4:
            self.ids.Match.source = 'images/Ene.png'

    def release(self):
        self.ids.Button_Image.source = 'images/Button_not_pressed.png'


# class SecondWindow(Screen):
#     pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('screen.kv')


class Flames(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == "__main__":
    Flames().run()
