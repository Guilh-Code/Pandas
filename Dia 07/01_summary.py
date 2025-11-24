# %%
import pandas as pd

# %%

clientes = pd.read_csv("../Data/clientes.csv", sep=";")
clientes

# %%

clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

# %%

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].sum()
clientes[redes_sociais].mean()

# %%

clientes.describe()
clientes.dtypes

# %%

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.to_list()
clientes[num_columns].sum()
clientes[num_columns].describe()

# %%


