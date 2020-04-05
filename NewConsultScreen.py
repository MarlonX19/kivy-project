from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import sqlite3

class NewConsultScreen(Screen): 
    
    def __init__(self, tarefas=[], **kwargs): #keywords arguments
        super().__init__(**kwargs)
          
    def newConsult(self):
        description = self.ids.description.text #pega o que o usuário digitou
        date = self.ids.date.text #pega o que o usuário digitou

        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("INSERT INTO consults (description, date) VALUES (?, ?)", (description, date))
            conn.commit()
        except Exception as e:
            print(e)
            popup = Popup(title='Atenção!', content=Label(text='Não foi possível registrar a consulta.'), size_hint=(None, None), size=(300, 200))
            popup.open()
            conn.rollback() 
        else:
            popup = Popup(title='Atenção!', content=Label(text='Consulta registrada com sucesso.'), size_hint=(None, None), size=(300, 200))
            popup.open()
        finally:
            conn.close()