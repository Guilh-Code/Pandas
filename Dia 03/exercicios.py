# %%
import pandas as pd

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")
df

# %%
filtro = df["flTwitch"] == 1
df[filtro]

# %%
filtro = df["qtdePontos"] >= 1000
df[filtro].shape
df[filtro]

# %%
df_2 = pd.read_csv("../Data/transacoes.csv", sep=";")
df_2

# %%
df_2["DtCriacao"] = pd.to_datetime(df_2["DtCriacao"])

filtro = df_2["DtCriacao"].dt.date == pd.to_datetime("2025-02-01").date()

df_2[filtro].shape

# %%
