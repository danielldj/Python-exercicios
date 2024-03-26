import random

def sorteios():
    sorteio = []
    for c in range(5):
        sorteio.append(random.randint(1,10))
    return sorteio

def par(n):
    cont = 0 
    for numero in numeros:
        if numero % 2 == 0:
            cont += numero
    return cont

numeros = sorteios()
soma_par = par(n=numeros)
print(f'Sorteando 5 valores da lista {numeros} pronto!')
print(f'somando os valores pares de {numeros} temos {soma_par}')