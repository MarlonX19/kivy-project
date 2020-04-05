
from kivy.app import App

from Gerenciador import Gerenciador

#chama o layout do Kivy
class Sample_app(App):
    def build(self):
        return Gerenciador() 