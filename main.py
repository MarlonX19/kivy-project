from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
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
        AllConsults.addNewConsult(texto) #adiciona na lista
        self.ids.texto.text = ''
        
class AllConsults(object):
    
     
    def __init__(self, listConsults=['teste']): 
        self.listConsults = listConsults
        
        
    @staticmethod
    def addNewConsult(texto=''):
        
        return AllConsults.addNew(texto)
             

    def addNew(self, texto=''):
        
        self.listConsults.append(texto)
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