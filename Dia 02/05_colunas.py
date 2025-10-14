# %%
import pandas as pd

df = pd.read_csv("../Data/transacoes.csv", sep=";")
df
# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
renamed_columns = {
    "QtdePontos": "qtPontos",                  "DescSistemaOrigem": "SistemaOrigem"
}

#df = df.rename(columns = renamed_columns)
df.rename(columns=renamed_columns, inplace=True)

# %%
df.info()

# %%
df[["IdCliente", "qtPontos"]]

# %%
# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].head()

# %%
# SELECT IdCliente, idTransacao, qtPontos FROM df LIMIT 5
df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)

# %%
colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df

# %%
 