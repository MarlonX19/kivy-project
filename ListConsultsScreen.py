from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

import sqlite3
        
class ListConsultsScreen(Screen): 
    def __init__(self, **kwargs): #keywords arguments
        super(ListConsultsScreen, self).__init__(**kwargs)
        
        
    def returnAllConsults(self):
        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("SELECT id, description, date, status FROM consults")
            rows = cur.fetchall()
            
            return rows
        except Exception as e:
            print(e)
            conn.rollback()
            return
        finally:
            conn.close()          

    def deleteConsult(self, btnId):
        idConsult = btnId.replace('btn', '')

        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            conn.commit()

            popup = Popup(title='Sucesso!', content=Label(text='Consulta deletada com sucesso!'), size_hint=(None, None), size=(300, 200))
            popup.open()

            self.on_pre_enter()
        except Exception as e:
            print(e)
            conn.rollback()
            return
        finally:
            conn.close() 

    def completeConsult(self, btnId):
        idConsult = btnId.replace('btn', '')
        
        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("UPDATE consults SET status = 1 WHERE id = {}".format(idConsult))
            conn.commit()
            
            popup = Popup(title='Sucesso!', content=Label(text='Consulta marcada como completa!'), size_hint=(None, None), size=(300, 200))
            popup.open()

            self.on_pre_enter()
        except Exception as e:
            print(e)
            conn.rollback()
            return
        finally:
            conn.close()


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

        consults = self.returnAllConsults()

        self.ids.boxlist.clear_widgets()

        for consult in consults:
            print(consult)
            if consult[1] != None and consult[2] != None: 
                self.ids.boxlist.add_widget(Label(text='Descrição: ' + consult[1] + '\n' + 'Consulta em: ' + consult[2], 
                                                  font_size=15, 
                                                  size_hint_y=None, 
                                                  height=150))  

                rowbuttons = BoxLayout(orientation='horizontal')

                btnDelete = Button(text='Excluir Consulta', 
                                    id='btn' + str(consult[0]),
                                    font_size=15, 
                                    size_hint_y=None, 
                                    height=40,
                                    background_color=(1.0, 0.0, 0.0, 1.0))
                btnDelete.bind(on_press=lambda x: self.deleteConsult(x.id))

                if consult[3] == 0:
                    btnComplete = Button(text='Concluir Consulta', 
                                    id='btn' + str(consult[0]),
                                    font_size=15, 
                                    size_hint_y=None, 
                                    height=40)
                    btnComplete.bind(on_press=lambda x: self.completeConsult(x.id))
                    rowbuttons.add_widget(btnComplete)

                rowbuttons.add_widget(btnDelete)

                self.ids.boxlist.add_widget(rowbuttons)

       
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
        
    def on_pre_leave(self):

        Window.unbind(on_keyboard=self.voltar) #desativa a funcionalidade da tecla