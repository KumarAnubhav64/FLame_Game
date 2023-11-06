# Flames App made on kivy framework by Kumar Anubhav
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

Window.size = (360, 700)
# define our differnt screen

class LoadWindow(Screen):
    def start_release(self):
        self.ids.Start.source = 'images/Start_re.png'
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
        fla = ["Frindship","Love","Affection","Marraige","Enemies"]
        flame = len(uncommon_char)
        ref_to_other_screen = self.manager.get_screen("ResultWindow")
        
        pos_flame = flame % 6
        if pos_flame == 0:
            ref_to_other_screen.ids.Result_Label.text= fla[0]
            ref_to_other_screen.ids.result_image.source= "images/Friend.png"
        elif pos_flame == 1:                                                                                                                                                        
            ref_to_other_screen.ids.Result_Label.text = fla[1]
            ref_to_other_screen.ids.result_image.source= "images/love.png"
        elif pos_flame == 2:
            ref_to_other_screen.ids.Result_Label.text = fla[2]
            ref_to_other_screen.ids.result_image.source= "images/Aff.png"
        elif pos_flame == 3:
            ref_to_other_screen.ids.Result_Label.text= fla[3]
            ref_to_other_screen.ids.result_image.source= "images/Marraige.png"
        elif pos_flame == 4:
            ref_to_other_screen.ids.Result_Label.text = fla[4]
            ref_to_other_screen.ids.result_image.source= "images/Ene.png"
        # if pos_flame == 0:
        #     self.manager.get_screen('ResultWindow').ids.
        # elif pos_flame == 1:                                                                                                                                                        
        #     self.ids.Match.text = fla[1]
        # elif pos_flame == 2:
        #     self.ids.Match.text = fla[2]
        # elif pos_flame == 3:
        #     self.ids.Match.text = fla[3]
        # elif pos_flame == 4:
        #     self.ids.Match.text = fla[4]

    def release(self):
        self.ids.Button_Image.source = 'images/Button_not_pressed.png'


class ResultWindow(Screen):
    def reset(self):
        ref_to_First_Window = self.manager.get_screen("first")
        ref_to_First_Window.ids.Him.text = 'Him'
        ref_to_First_Window.ids.Her.text = 'Her'
        self.ids.Button_Image.source = 'images/Reset_on_press.png'
    
    def release(self):
        self.ids.Button_Image.source = 'images/Reset_on_release.png'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('screen.kv')


class Flames(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == "__main__":
    Flames().run()
