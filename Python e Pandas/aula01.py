import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas  - 2017.csv', sep=';')


prdutos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
print(prdutos_quantidade)