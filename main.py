from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

import sqlite3

#importando classes/modulods
import NewConsultScreen
import MenuScreen
import Connection
import AllConsults
import RescheduleConsultScreen
import CancelConsultScreen
import ListConsultsScreen
import LoginScreen
from Gerenciador import Gerenciador
from Sample_app import Sample_app



    
  
Sample_app().run()
