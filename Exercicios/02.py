# %%
import pandas as pd

transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")
transacoes.head()

# %%

transacoes["Valores_1"] = 1
transacoes

# %%
