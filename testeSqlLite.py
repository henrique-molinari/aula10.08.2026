import sqlite3

# Criar ou conectar ao banco local
conexao = sqlite3.connect("integracao_dados.db")
cursor = conexao.cursor()

# Criar tabela para consolidar dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fonte TEXT NOT NULL,
    dado TEXT NOT NULL
)
""")
print("Tabela criada com sucesso para integração!")
conexao.close()
    