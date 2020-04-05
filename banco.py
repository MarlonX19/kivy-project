import sqlite3

conn = sqlite3.connect('consultas.db')
cursor = conn.cursor()

# leitura dos dados
cursor.execute("""
SELECT * FROM consultas;
""")

#percorre todos os dados
for linha in cursor.fetchall():
    print(linha)

#fechando a conexão
conn.close()