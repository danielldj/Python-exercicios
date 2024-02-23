import pandas as pd
import numpy
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()
carteira = pd.read_excel('Carteira.xlsx')
print(carteira)

#Criando nosso datafreme de cotações dos ativos da carteira

cotacoes_carteira = pd.DataFrame()

for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = web.get_data_yahoo('{}.SA'.format(ativo), start='2020-01-01', end='2020-11-10')['Adj Close']
print(cotacoes_carteira)

#VERIFICANDO SE TODOS OS DADOS VIERAM CORRETOS
cotacoes_carteira.info()

#AJUSTANDO OS DADOS

#com media

#df_media = cotacoes_carteira.mean()
#cotacoes_carteira = cotacoes_carteira.fillna(df_media)

#com ultimo valor

cotacoes_carteira = cotacoes_carteira.ffill()
cotacoes_carteira.info()

#VAMOS VER COMO AS AÇÕES FORAM INDIVIDUALMENTE

carteira_norm = cotacoes_carteira / cotacoes_carteira.iloc[0]
carteira_norm.plot(figsize=(15, 5))
plt.legend(loc='upper left')
plt.show()

#VAMOS PUXAR O IBOV PARA COMPARAR
cotacao_ibov = web.get_data_yahoo('^BVSP', start='2020-01-01', end='2020-11-10')

#CRIANDO UM DATAFRAME DA CARTEIRA COM AS QUANTIDADES DAS AÇÕES

valor_investido = pd.DataFrame()

for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos'] == ativo, 'Qtde'].values[0]
print(valor_investido)

#COMPARANDO CARTEIRA X IBOV
valor_investido['Total'] = valor_investido.sum(axis=1)

valor_ivestido_norm = valor_investido / valor_investido.iloc[0]
cotacao_ibov_norm = cotacao_ibov / cotacao_ibov.iloc[0]

valor_ivestido_norm['Total'].plot(figsize=(15, 5), label='Carteira')
cotacao_ibov_norm['Adj Close'].plot(figsize=(15, 5), label='IBOV')
plt.legend()
plt.show()


#CORRELAÇÃO ENTRE A CARTEIRA E O IBOV

correlacao = valor_investido['Total'].corr(cotacao_ibov['Adj Close'])
print(correlacao)