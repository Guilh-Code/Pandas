# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")
df.head()

# %%
df["pontos_100"] = df["qtdePontos"] + 100

# %%
df.head()

# %%
df["EmailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%

df["QtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%

df["Todas_Social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%
df["qtdePontos"].describe()

# %%
df["logPontos"] = np.log(df["qtdePontos"] + 1)
df["logPontos"].describe()

# %%
import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()

# %%

