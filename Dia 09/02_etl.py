# %%

import pandas as pd
import sqlalchemy

from sklearn import cluster

# %%

with open("etl.sql") as open_file:
    query = open_file.read()

# %%

engine = sqlalchemy.create_engine("sqlite:///../database.db")

df = pd.read_sql_query(query, con=engine)
df

# %%

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["flTwitch", "qtdePontos"]])


df["cluster"] = kmean.labels_
df

# %%

df.to_sql("sellers_cluster", 
          con=engine, 
          index=False,
          if_exists="replace")

# %%
