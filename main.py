from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')

from kivy.core.window import Window
Window.clearcolor = (.9, .20, .17, 1)


class App(App):
    def build(self):
        return Label(text='Hello world')

test = App()

test.run()
