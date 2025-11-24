# %%
import pandas as pd

# %%

df = pd.read_csv("../Data/clientes.csv", sep=";")
df.head()
# %%

def get_last_id(x):
    return x.split("-")[-1]

df["idCliente"].apply(get_last_id)

# %%
 