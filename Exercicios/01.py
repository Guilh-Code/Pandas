# %%

# 06.04 - Quem teve mais transações de Streak?

import pandas as pd
# %%

transacoes = pd.read_csv("../Data/transacoes.csv", sep=";")
transacoes.head()

# %%

transacao_produto = pd.read_csv("../Data/transacao_produto.csv", sep=";")
transacao_produto.head()

# %%

produto = pd.read_csv("../Data/produtos.csv", sep=";")
produto.head()

# %%

cliente_transacao_produto = transacoes.merge(transacao_produto,
                 on="IdTransacao",
                 how='left')[['IdTransacao', "IdCliente", "IdProduto"]]

# %%

cliente_transacao_produto["IdProduto"] = (
    pd.to_numeric(cliente_transacao_produto["IdProduto"], errors="coerce")
    .astype("Int64")
)

# %%

cliente_transacao_produto.dtypes

# %%

df_full = cliente_transacao_produto.merge(
    produto,
    on=["IdProduto"]
)


# %%

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]


# %%

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)

# %%

produtos = produto[produto["DescNomeProduto"]=="Presença Streak"][["IdProduto", "DescNomeProduto"]]

# %%

(transacoes.merge(
    transacao_produto,
    on="IdTransacao",
    how='left'
    ).merge(produtos, on=["IdProduto"], how='right')
    .groupby(by=["IdCliente"])["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# %%
