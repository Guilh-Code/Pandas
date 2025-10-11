# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

series_idades = pd.Series(idades)
series_idades
# %%

idades[-1]
series_idades[2]
# %%

series_idades[-1]
# %%

series_idades = series_idades.sort_values(ascending=False)

series_idades
# %%

series_idades.iloc[0]
# %%
series_idades.iloc[-1]
# %%
series_idades.iloc[:3]
# %%
series_idades.iloc[::-1]
# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

index = [
    "Gui1", "Gui2", "Gui3", "Gui4", "Gui5",
    "Gui6", "Gui7", "Gui8", "Gui9", "Gui10",
    "Gui11", "Gui12", "Gui13", "Gui14", "Gui14"
]

series_idades = pd.Series(idades, index=index)
series_idades

# %%

series_idades["Gui11"]
# %%
series_idades.iloc[0]
# %%
series_idades["Gui14"]
# %%
series_idades.loc["Gui12"]
# %%
series_idades.iloc[[-1]]
# %%
