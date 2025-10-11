# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Gui1", "Gui2", "Gui3", "Gui4", "Gui5",
    "Gui6", "Gui7", "Gui8", "Gui9", "Gui10",
    "Gui11", "Gui12", "Gui13", "Gui14", "Gui14"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

series_idades
series_nomes

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

# %%

df.iloc[0]["nomes"]
# %%

df.iloc[-1]["idades"]
# %%
