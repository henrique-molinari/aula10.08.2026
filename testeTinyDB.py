# python testeTinyDB.py

from tinydb import TinyDB

# # Criar banco de dados de teste
# db = TinyDB('teste.json')
# print("TinyDB instalado e funcionando corretamente!")


# # Criar ou conectar ao banco de dados
# db = TinyDB('dados.json')

# # Criar tabelas
# usuarios = db.table('usuarios')
# produtos = db.table('produtos')

print("Tabelas criadas com sucesso!")


def adicionar_usuario(nome, idade):
    usuarios = TinyDB("dados.json").table("usuarios")
    usuarios.insert({"nome": nome, "idade": idade})
    print(f"Usuário {nome} adicionado com sucesso!")


def adicionar_produto(nome, preco):
    produtos = TinyDB("dados.json").table("produtos")
    produtos.insert({"nome": nome, "preco": preco})
    print(f"Produto {nome} adicionado com sucesso!")

# Exemplo de uso:
adicionar_usuario("Max", 30)
adicionar_produto("Notebook", 2500)
