from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from AllConsults import AllConsults

class NewConsultScreen(Screen): 
    
    def __init__(self, tarefas=[], **kwargs): #keywords arguments
        super().__init__(**kwargs)
        
        
    def addWidget(self):
        texto = self.ids.texto.text #pega o que o usuário digitou
        print('texto digitado: ' + texto)
        # ListConsultsScreen.ids.box.add_widget(Consult(text=texto)) 
        # #adiciona na lista

        #Instancia a classe de consulta e no construtor ja passa o texto
        allCon = AllConsults(texto) 
        # acredito não ser necessário esse método
        #allCon.addNewConsult(texto) 
        self.ids.texto.text = ''