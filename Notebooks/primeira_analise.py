from pathlib import Path
import pandas as pd

pasta = Path(__file__).resolve().parent
produtos = pd.read_csv(pasta / "produtos.csv")
movimentacoes = pd.read_csv(pasta / "movimentacoes.csv", parse_dates=["data"])
estoques = pd.read_csv(pasta / "estoques.csv", parse_dates=["data"])
fornecedores = pd.read_csv(pasta / "fornecedores.csv")

print("Quantidade de produtos:", len(produtos))
print("Quantidade de registros de movimentação:", len(movimentacoes))
print("\nPrimeiros produtos:")
print(produtos.head())
print("\nTotal de saídas por categoria:")
analise = movimentacoes.merge(produtos[["sku", "categoria"]], on="sku")
print(analise.groupby("categoria")["saidas"].sum().sort_values(ascending=False))
print("\nÚltima data disponível:", movimentacoes["data"].max().date())
