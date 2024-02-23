import pandas as pd
import numpy
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()

carteira = pd.read_excel('FUNDOS_FII.xlsx')

cotacoes_carteira = pd.DataFrame()

for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = web.get_data_yahoo('{}.SA'.format(ativo), start='2023-01-01', end='2023-12-12')['Adj Close']

print(cotacoes_carteira)

cotacoes_carteira.info()

cotacoes_carteira = cotacoes_carteira.ffill()
cotacoes_carteira.info()


cotacoes_carteira_norm = cotacoes_carteira / cotacoes_carteira.iloc[0]
cotacoes_carteira_norm.plot(figsize=(15, 5))
plt.legend(loc='upper left')
plt.show()

cotacao_ibov = web.get_data_yahoo('^BVSP', start='2023-01-01', end='2023-12-12')

valor_investido = pd.DataFrame()

for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos'] == ativo, 'Qtde'].values[0]
print(valor_investido)

valor_investido['Total'] = valor_investido.sum(axis=1)

cotacao_ibov_norm = cotacao_ibov / cotacao_ibov.iloc[0]
valor_ivestido_norm = valor_investido / valor_investido.iloc[0]

valor_ivestido_norm['Total'].plot(figsize=(15, 5), label='Carteira')
cotacao_ibov_norm['Adj Close'].plot(figsize=(15, 5), label='IBOV')
plt.legend()
plt.show()

correlacao = valor_investido['Total'].corr(cotacao_ibov['Adj Close'])
print(correlacao)
