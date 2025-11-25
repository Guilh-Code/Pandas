# %%
import pandas as pd

clientes = pd.read_csv("../Data/clientes.csv", sep=";")
clientes

# %%

clientes[clientes["flTwitch"] == 1].shape[0]

# %%

clientes[clientes["qtdePontos"] >= 1000].shape[0]

clientes.shape[0]

# %%

transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")


# %%

transacoes["DtCriacao"] = pd.to_datetime(transacoes["DtCriacao"])
transacoes[transacoes["DtCriacao"].dt.date == pd.to_datetime("2025-02-01").date()].shape[0]

# %%
