from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

import sqlite3

from Connection import Connection

class AllConsults(list):
    def __init__(self, consult=['teste']):
        self.listConsults = [] #Cria a lista
        self.addNew(consult) #Chama método para adicionar e passa o texto digitado
        
    @staticmethod
    def addNewConsult(texto=''):
        return AllConsults.addNew(texto)     

    def addNew(self, texto=['nome', 'marlon']):
        try:
            conn = sqlite3.connect('consultas.db', isolation_level=None)
            cursor = conn.cursor()
            print(cursor)
        except IOError as e:
            print(e)

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

            Connection()
            cur = conn.cursor()
            sqlite_query = """INSERT INTO consultas
                          (description) 
                          VALUES (?);"""
            custom_data = (texto)

            cur.execute(sqlite_query, (custom_data,))
            Connection.conn.commit()
            cur.execute("SELECT * FROM consultas")
 
            rows = cur.fetchall()
 
            for row in rows:
                print(row)

            #fechando a conexão
            #conn.close()

        return self.listConsults
        
    @staticmethod  
    def getList():
        pass
      #  return AllConsults.getListConsults()
    
    def getListConsults(self):
        return self.listConsults
        
        