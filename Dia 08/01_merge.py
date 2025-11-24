# %%
import pandas as pd

transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")
transacoes.columns = ["IdTransacao", "idCliente", "DtCriacao", "QtdePontos", "DescSistemaOrigem"]
transacoes.head()

# %%

clientes = pd.read_csv("../Data/clientes.csv", sep=";")
clientes.head()

# %%

transacoes.merge(right=clientes,
                 how='left',
                 on=['idCliente'],
                 suffixes=["Transacao", "Cliente"]
                 )

# df1.merge(df2, left_on=["idCliente"], right_on=["id"],
#           how='left')

# %%
