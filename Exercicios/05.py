# %%

import pandas as pd

clientes = pd.read_csv("../Data/clientes.csv", sep=";")
clientes.head()

# %%

clientes["twitch_points"] = clientes["qtdePontos"] * clientes["flTwitch"]

# %%

id_maior = clientes.loc[clientes["qtdePontos"].idxmax(), "idCliente"]
id_menor = clientes.loc[clientes["qtdePontos"].idxmin(), "idCliente"]

# %%

print("Maior saldo:", id_maior)
print("Menor saldo:", id_menor)

# %%
