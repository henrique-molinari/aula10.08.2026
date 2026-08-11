# python testepandas.py

import pandas as pd

data = {
    "Nome": ["Ana", "Carlos", "Maria", "João"],
    "Idade": [25, 30, 28, 22],
    "Cidade": ["SP", "RJ", "BH", "POA"],
}

df = pd.DataFrame(data)

# Soma
print(df["Idade"].sum())

# Média
print(df["Idade"].mean())

# Agrupamento
print(df.groupby("Cidade")["Idade"].mean())

# Salvar para CSV
df.to_csv('dados.csv', index=False)

