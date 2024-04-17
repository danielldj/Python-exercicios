import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas  - 2017.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas',sep=';')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos',sep=';')
clientes_df = pd.read_csv('Contoso - Clientes',sep=';')

print(vendas_df)