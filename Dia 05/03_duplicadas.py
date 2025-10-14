# %%
import pandas as pd

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")

# %%
df = df.sort_values("salario", ascending=False).drop_duplicates(keep="last" ,subset=["nome", "sobrenome"])
df
