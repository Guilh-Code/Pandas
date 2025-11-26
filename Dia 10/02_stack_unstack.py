# %%

import pandas as pd

df = pd.read_csv("...")
df.head()

# %%

df_stack = df.set_index(["nome", "periodo"]).stack()

df_stack = df_stack.reset_index()

df_stack.columns = ["nome", "periodo", "metrica", "valor"]

df_stack

# %%

df_unstack = (df_stack.set_index(["nome", "periodo", "metrica"]).unstack().reset_index())

df_unstack.columns

# %%

metricas = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ["nome", "periodo"] + metricas
df_unstack
