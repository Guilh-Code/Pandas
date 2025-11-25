# %%

import pandas as pd

clientes = pd.read_csv("../Data/clientes.csv", sep=";")
clientes.info()

# %%

clientes.describe()
clientes.dtypes
clientes.shape

# %%

transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")
transacoes.info()

# %%

produtos = pd.read_csv("../Data/produtos.csv", sep=";")
produtos.info()

# %%

clientes["idCliente"].iloc[4]
clientes.head()

# %%

clientes[["idCliente", "qtdePontos"]].iloc[10]

# %%
