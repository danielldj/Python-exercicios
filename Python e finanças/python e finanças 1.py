import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns


import yfinance as yf
yf.pdr_override()
ibov = web.get_data_yahoo('^BVSP', start='2020-01-01', end='2020-11-10')
print(ibov)

ibov['Adj Close'].plot(figsize=(15, 5))

#Retorno IBOV

retorno_ibov = ibov['Adj Close'][-1] / ibov['Adj Close'][0] - 1
print(f'Retorno IBOV : {retorno_ibov:.2%}')

#Analisando com Média Movel

ibov['Adj Close'].plot(figsize=(15, 5), label='IBOV')
plt.show()
ibov['Adj Close'].rolling(21).mean().plot(label='MM21')
plt.legend()
plt.show()





