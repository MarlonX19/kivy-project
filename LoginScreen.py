from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from datetime import date


import sqlite3

class LoginScreen(Screen): 
    def __init__(self, **kwargs): #keywords arguments
        super().__init__(**kwargs)
                 
    def login(self):
        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            return

        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("SELECT name, password FROM users WHERE name = ? and password = ?", (username, password,))
            rows = cur.fetchall()
            
            if len(rows) > 0:
                App.get_running_app().root.current = 'menu'
            else:
                popup = Popup(title='Atenção!', content=Label(text='Usuário ou senha incorretos!'), size_hint=(None, None), size=(300, 200))
                popup.open()
        except Exception as e:
            print(e)
            popup = Popup(title='Atenção!', content=Label(text='Erro na autenticação!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            conn.rollback()
            return
        finally:
            conn.close()
        try: # Cria arquivo de consulta
            with open('log.txt', 'a+') as file:
                file.write("O usuário " + username + " entrou no sistema na data " + str(date.today()) + "\n") 
        except IOError as e:
            print(e)
           
        
    def register(self):
        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            return

        try:
            conn = sqlite3.connect('DBApp.db')
            cur = conn.cursor()

            cur.execute("SELECT name FROM users WHERE name = ?", (username,))
            rows = cur.fetchall()
            
            if len(rows) > 0:
                popup = Popup(title='Atenção!', content=Label(text='Usuário já existe!'), size_hint=(None, None), size=(300, 200))
                popup.open()
                conn.close()
                return

            cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (username, password,))

            conn.commit()
        except Exception as e:
            print(e)
            popup = Popup(title='Atenção!', content=Label(text='Erro ao tentar registrar um usuário!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            conn.rollback()
            return
        else:
            popup = Popup(title='Atenção!', content=Label(text='Usuário criado com sucesso.\nAutentique-se!'), size_hint=(None, None), size=(300, 200))
            popup.open()
        finally:
            conn.close()