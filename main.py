from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView

import sqlite3

#chamada de conexão ao banco de dados
class Connection():

    def __init__(self):
        self.conn = sqlite3.connect('DBApp.db')
        self.cursor = conn.cursor()

    #popular dados inseridos no campo de consultas
    #utilizando o comando comando INSERT 
    #cursor.execute("INSERT INTO consultas (description) VALUES(%s)", (description))
    #con.commit()

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
               

    
class ListConsultsScreen(Screen): 
    def __init__(self, consultas=[], **kwargs): #keywords arguments
        super().__init__(**kwargs)
        
       # consultas = AllConsults.getList()
        
        for consulta in consultas:   
            print('item: ' + consulta)
            #self.ids.box.add_widget(Consult(text=consulta))
            
            
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
       
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
        
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar) #desativa a funcionalidade da tecla


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


class Manager(ScreenManager):
    pass

class MenuScreen(Screen):
    pass
      
class ConsultsApp(App):
    def build(self):
        Builder.load_string(open("LayoutsScreens.kv", encoding="utf-8").read(), rulesonly=True)
        return Manager() 
    

ConsultsApp().run()
