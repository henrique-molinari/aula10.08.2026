# python testepandas.py

import pandas as pd

# Criando um DataFrame
data = {
    "Nome": ["Ana", "Carlos", "Maria", "João"],
    "Idade": [25, 30, 28, 22],
    "Cidade": ["SP", "RJ", "BH", "POA"],
}

df = pd.DataFrame(data)
# print(df)

# Primeiras linhas
print(df.head(2))

# Últimas linhas
print(df.tail(2))

# Informações do DataFrame
print(df.info())

# Estatísticas descritivas
print(df.describe())