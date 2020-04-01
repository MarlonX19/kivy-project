import kivy   
from kivy.app import App  
from kivy.lang import Builder   
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
   
Builder.load_string(""" 
<MenuScreen>: 
    BoxLayout: 
        orientation: 'vertical'
        GridLayout:
            cols: 1
            Button: 
                text: "CADASTRAR CONSULTA" 
                font_size: 25
                background_color : 0, 0, 1, 1 
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 0.3 
                    root.manager.current = 'new_consult_screen' 
            Button: 
                text: "HISTÓRICO DE CONSULTAS" 
                font_size: 25
                background_color : 0, 0, 1, 1 
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 0.3  
                    root.manager.current = 'list_consults_screen' 
            Button: 
                text: "REAGENDAR CONSULTA" 
                font_size: 25
                background_color : 0, 0, 1, 1 
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 0.3  
                    root.manager.current = 'reschedule_consult_screen' 
            Button: 
                text: "CANCELAR CONSULTA" 
                font_size: 25
                background_color : 0, 0, 1, 1 
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 0.3  
                    root.manager.current = 'cancel_consult_screen' 
 
<NewConsultScreen>: 
    GridLayout:
        cols: 1
        GridLayout:
            size_hint_y: 0.6
            cols: 2
            Label:
                text: 'Seu nome'
                markup: True
                shorten: True
                ellipsis_options: {'color':(1,0.5,0.5,1),'underline':True}
            TextInput:
                height: self.minimum_height
                multiline: False
                id: txt_input
        Button: 
            text: "VOLTAR AO MENU" 
            font_size: 25
            background_color : 0, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.transition.duration = 0.3  
                root.manager.current = 'menu_screen'

<ListConsultsScreen>: 
    GridLayout:
        cols : 1
        Button: 
            text: "VOLTAR AO MENU" 
            font_size: 25
            background_color : 0, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.transition.duration = 0.3  
                root.manager.current = 'menu_screen'

<RescheduleConsultScreen>: 
    GridLayout:
        cols : 1
        Button: 
            text: "VOLTAR AO MENU" 
            font_size: 25
            background_color : 0, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.transition.duration = 0.3  
                root.manager.current = 'menu_screen'

<CancelConsultScreen>: 
    GridLayout:
        cols : 1
        Button: 
            text: "VOLTAR AO MENU" 
            font_size: 25
            background_color : 0, 0, 1, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.transition.duration = 0.3  
                root.manager.current = 'menu_screen'

""") 
   

class MenuScreen(Screen): 
    pass
   
class NewConsultScreen(Screen): 
    pass

class ListConsultsScreen(Screen): 
    pass
  
class RescheduleConsultScreen(Screen): 
    pass

class CancelConsultScreen(Screen): 
    pass
   

screen_manager = ScreenManager() 
   
screen_manager.add_widget(MenuScreen(name ="menu_screen")) 
screen_manager.add_widget(NewConsultScreen(name ="new_consult_screen")) 
screen_manager.add_widget(ListConsultsScreen(name ="list_consults_screen")) 
screen_manager.add_widget(RescheduleConsultScreen(name ="reschedule_consult_screen")) 
screen_manager.add_widget(CancelConsultScreen(name ="cancel_consult_screen")) 
  

class ScreenApp(App): 
    def build(self): 
        return screen_manager 
  

sample_app = ScreenApp() 
sample_app.run() 
