from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# classe Tarefa
class Consult(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text