from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

import sqlite3


class ReportsScreen(Screen): 
    def __init__(self, **kwargs): #keywords arguments
        super().__init__(**kwargs)

        
    def returnInfo(self):
        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("""select case status 
                                  when 1 then 'Finalizada' 
                                  when 0 then 'Agendada' 
                                  end status, 
                                  count(status) 
                             from consults
                            group by status""")
            rows = cur.fetchall()
            
            return rows
        except Exception as e:
            print(e)
            conn.rollback()
            return
        finally:
            conn.close()          

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
        
        infos = self.returnInfo()

        self.ids.boxreport.clear_widgets()

        self.ids.boxreport.add_widget(Label(text='CONSULTAS FINALIZADAS: ' + str(infos[1][1]), 
                                    font_size=30))  
        
        self.ids.boxreport.add_widget(Label(text='CONSULTAS NÃO' + '\n' + 'FINALIZADAS: ' + str(infos[0][1]), 
                                    font_size=30))  

       
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
        
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar) #desativa a funcionalidade da tecla