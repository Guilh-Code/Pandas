# %%
import pandas as pd

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")
df.head()

# %%
Top_5 = (df.sort_values(by="qtdePontos", ascending=False).head()["idCliente"])
Top_5

# %%

