from kivy.app import App

import sqlite3

#chamada de conexão ao banco de dados
class Connection():

    def __init__(self):
        self.conn = sqlite3.connect('DBApp.db')
        self.cursor = self.conn.cursor()