from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')

from kivy.core.window import Window
Window.clearcolor = (.12, .20, .17, 1)


class FirstLayout(BoxLayout):
    pass
    

class App(App):
    def build(self):
        return FirstLayout()

test = App()
test.run()
