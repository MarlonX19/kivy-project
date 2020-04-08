from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

import sqlite3
        
class ListConsultsScreen(Screen): 
    def __init__(self, **kwargs): #keywords arguments
        super(ListConsultsScreen, self).__init__(**kwargs)
        
        
    def returnAllConsults(self):
        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("SELECT id, description, date FROM consults")
            rows = cur.fetchall()
            
            return rows
        except Exception as e:
            print(e)
            conn.rollback()
            return
        finally:
            conn.close()  

    def removeConsult(self, idConsult):
        print(idConsult)


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

        consults = self.returnAllConsults()
        self.ids.boxlist.clear_widgets()
        for consult in consults:
            if consult[1] != None and consult[2] != None: 
                self.ids.boxlist.add_widget(Label(text='Descrição: ' + consult[1] + '\n' + 'Consulta em: ' + consult[2], 
                                                  font_size=15, 
                                                  size_hint_y=None, 
                                                  height=100))  
                self.ids.boxlist.add_widget(Button(text='Excluir Consulta', 
                                font_size=15, 
                                size_hint_y=None, 
                                height=40,
                                on_press=lambda x: self.removeConsult(consult[0])))

       
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
        
    def on_pre_leave(self):

        Window.unbind(on_keyboard=self.voltar) #desativa a funcionalidade da tecla