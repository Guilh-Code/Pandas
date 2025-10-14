# %%
import pandas as pd

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")
df.head()

# %%
df.dropna()
df.dropna(how="any") # Ou "all"
df.dropna(how="any", subset=["DtCriacao"]) # Exemplo excluir NaN de certas coluans

df["idade"].fillna(0)

df.fillna({"nome": "alguem", "idade": 0})

medias = df[["idade", "salario"]].mean()
df.fillna(medias)

# %%
