# %%
import pandas as pd

# %%
df = pd.read_csv("../Data/clientes.csv", sep=";")
df.head()

# %%
df["qtdePontos"].astype(float)

# %%
pd.to_datetime(df["DtCriacao"].replace({
    #"Valor_Antigo" : "Valor_Novo"
}))

# %%
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])

# %%
df["DtCriacao"].dt.year
# day
# month
# month_name()
# day_of_week
# date

# %%
