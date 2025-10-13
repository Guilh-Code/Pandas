# %%
import pandas as pd

df_clientes = pd.read_csv("../Data/clientes.csv", sep=';')
df_clientes
# %%
# AMOSTRAS

# Começo
df_clientes.head(n=10)

# %%
# Final
df_clientes.tail()

# %%
# Aleatório
df_clientes.sample(10)

# -----------------------------------------

# %%
df_clientes.shape

# %%
df_clientes.columns

# %%
df_clientes.index

# %%
df_clientes.info(memory_usage="deep")

# %%
df_clientes.dtypes["qtdePontos"]

# %%

