from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class LoginScreen(Screen): 
    def __init__(self, **kwargs): #keywords arguments
        super().__init__(**kwargs)
                 
    def login(self):
        users = []

        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(200, 200))
            popup.open()
            return

        try:
            with open('users.txt') as file:
                usersArq = file.read().splitlines()
        except IOError as e:
            print(e)
            return    

        for userArq in usersArq:
            users.append((userArq.split()))

        user = list(filter(lambda x: x[0] == username, users))

        if len(user) > 0:
            if user[0][0] == username and user[0][1] == password:
                App.get_running_app().root.current = 'menu'
            else:
                popup = Popup(title='Atenção!', content=Label(text='Usuário ou senha inválidos!'), size_hint=(None, None), size=(200, 200))
                popup.open()
        else:
            popup = Popup(title='Atenção!', content=Label(text='Não encontramos o usuário!'), size_hint=(None, None), size=(200, 200))
            popup.open()
            
        
    def register(self):
        users = []

        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(200, 200))
            popup.open()
            return

        try:
            with open('users.txt', 'r') as file:
                usersArq = file.read().splitlines()

            for userArq in usersArq:
                if userArq.split()[0] == username:
                    popup = Popup(title='Atenção!', content=Label(text='Usuário já existe!'), size_hint=(None, None), size=(200, 200))
                    popup.open()
                    return

            with open('users.txt', 'a') as file:
                users = []
                if len(usersArq) == 0:
                    users.append(username + ' ' + password)
                else:
                    users.append('\n' + username + ' ' + password)
                file.writelines(users)
        except IOError as e:
            print(e)
            return
        else:
            popup = Popup(title='Atenção!', content=Label(text='Usuário criado com sucesso.\nAutentique-se!'), size_hint=(None, None), size=(200, 200))
            popup.open()
        