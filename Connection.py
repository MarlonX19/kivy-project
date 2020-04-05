from kivy.app import App

import sqlite3


#chamada de conexão ao banco de dados
class Connection():
    conn = sqlite3.connect('consultas.db')

    #populando dados inseridos no campo de consultas
    