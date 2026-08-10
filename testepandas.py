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

# # Selecionar uma coluna
# print(df["Nome"])

# # Selecionar múltiplas colunas
# print(df[["Nome", "Idade"]])

# # Selecionar linhas por índice
# print(df.iloc[1])  # Segunda linha
# print(df.iloc[1:3])  # Linhas 2 e 3

# # Selecionar por condição
# print(df[df['Idade'] > 25])

# Adicionar nova coluna
df['Salário'] = [5000, 6000, 5500, 4500]
print(df)

# Remover coluna
df = df.drop('Salário', axis=1)
print(df)

# Renomear colunas
df = df.rename(columns={'Cidade': 'Cidade'})
print(df)