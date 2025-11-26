# %%
import pandas as pd
import os

# %%

def read_file(file_name: str):
    df = (pd.read_csv(f"../Data/dataset/{file_name}.csv", sep=";")
          .rename(columns={"valor": file_name})
          .set_index(["nome", "periodo"])
          .drop(["cod"], axis=1))
    
    return df

# %%

file_names = os.listdir("../Data/dataset")

dfs = []

for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))

# %%

df_full = pd.concat(dfs, axis=1)
            .reset_index()
            .sort_values(["periodo", "nome"])

df_full.to_csv("homicios_consolidados.csv", index=False, sep=";")
