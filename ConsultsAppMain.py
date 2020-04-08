#importando classes/modulos
from kivy.app import App
from kivy.lang.builder import Builder

import NewConsultScreen
import MenuScreen
import Connection
import ListConsultsScreen
import LoginScreen
import ReportsScreen
from Manager import Manager        
      
class ConsultsApp(App):
    def build(self):
        Builder.load_string(open("LayoutsScreens.kv", encoding="utf-8").read(), rulesonly=True)
        return Manager() 
    

ConsultsApp().run()
