from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class NewConsultScreen(Screen): 
    
    def __init__(self, tarefas=[], **kwargs): #keywords arguments
        super().__init__(**kwargs)
        
        
    def addWidget(self):
        texto = self.ids.texto.text #pega o que o usuário digitou
        print('texto digitado: ' + texto)
        # ListConsultsScreen.ids.box.add_widget(Consult(text=texto)) #adiciona na lista
        allCon = AllConsults(texto) #Instancia a classe de consulta e no construtor ja passa o texto
        #allCon.addNewConsult(texto) # acredito não ser necessário esse método
        self.ids.texto.text = ''
        
class AllConsults(list):
    
    def __init__(self, consult=['teste']):
        self.listConsults = [] #Cria a lista
        self.addNew(consult) #Chama método para adicionar e passa o texto digitado
        
    @staticmethod
    def addNewConsult(texto=''):
        return AllConsults.addNew(texto)
             

    def addNew(self, texto=['nome', 'marlon']):
        self.listConsults.append(texto) # aqui de fato faz o append na lista

        try: # Cria arquivo de consulta
            with open('consults.txt', 'a+') as file:
                file.write(texto + "\n") 

        except IOError as e:
            print(e)
            return
        else:
            popup = Popup(title='Atenção!', content=Label(text='Consulta registrada com sucesso.'), size_hint=(None, None), size=(300, 200))
            popup.open()

        return self.listConsults
        
    @staticmethod  
    def getList():
        pass
      #  return AllConsults.getListConsults()
    
    
    def getListConsults(self):
        return self.listConsults
        
        
    
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
        users = []

        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(300, 200))
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
                popup = Popup(title='Atenção!', content=Label(text='Usuário ou senha inválidos!'), size_hint=(None, None), size=(300, 200))
                popup.open()
        else:
            popup = Popup(title='Atenção!', content=Label(text='Não encontramos o usuário!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            
        
    def register(self):
        users = []

        username = self.ids.nameInput.text
        password = self.ids.passInput.text

        if username.strip() == '' or password.strip() == '':
            popup = Popup(title='Atenção!', content=Label(text='Preencha todos os campos!'), size_hint=(None, None), size=(300, 200))
            popup.open()
            return

        try:
            with open('users.txt', 'r') as file:
                usersArq = file.read().splitlines()

            for userArq in usersArq:
                if userArq.split()[0] == username:
                    popup = Popup(title='Atenção!', content=Label(text='Usuário já existe!'), size_hint=(None, None), size=(300, 200))
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
            popup = Popup(title='Atenção!', content=Label(text='Usuário criado com sucesso.\nAutentique-se!'), size_hint=(None, None), size=(300, 200))
            popup.open()
        
        
  
class RescheduleConsultScreen(Screen): 
    pass

class CancelConsultScreen(Screen): 
    pass
   


# classe Tarefa
class Consult(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

      
class Sample_app(App):
    def build(self):
        return Gerenciador() 
    
  

Sample_app().run()
