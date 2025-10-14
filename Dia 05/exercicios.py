# %%
import pandas as pd

# %%
transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")
transacoes.head()

# %%
transacoes = transacoes.sort_values(by="DtCriacao")

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

# %%

transacoes.sort_values(by=["QtdePontos"], ascending=False).head(1)

# %%
