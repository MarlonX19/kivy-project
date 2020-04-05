from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

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