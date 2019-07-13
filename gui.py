from calculos import Calculos
import kivy
from kivy.clock import Clock
from kivy.app import App
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class RootLayout(BoxLayout):
    def anime_btns(self):
        Clock.schedule_once(self.anime_btn1, 1)
        Clock.schedule_once(self.anime_btn2, 2)
        Clock.schedule_once(self.anime_btn3, 3)
    def anime_btn1(self, *args):
        anim = Animation(opacity = 0.9, duration= 1)
        anim.start(self.ids.btn1)
    def anime_btn2(self, *args):
        anim = Animation(opacity = 0.9, duration= 1)
        anim.start(self.ids.btn2)
    def anime_btn3(self, *args):
        anim = Animation(opacity = 0.9, duration= 1)
        anim.start(self.ids.btn3)
class Janela(App):
    def build(self):
        Window.minimun_height = 600
        Window.minimun_width = 800
        self.title = "Orçamento Brasileiro"
        lay = RootLayout()
        lay.anime_btns()
        return lay
class main:
    if __name__ == '__main__':
        root = Janela()
        root.run()
