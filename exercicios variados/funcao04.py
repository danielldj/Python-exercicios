def fatorial(n , show= True):

    soma  = 0
    cont = n
    while cont > 1:
        soma = n * (cont-1)
        if show == True:
            if cont == n:
                print(f'{n} x {cont-1}', end=' ')
            else:
                print(f'x {cont-1}', end=' ')
        cont -= 1
        n = soma
    
    print(soma)
    print('-'*30)
n = int(input('valor: '))    
fatorial(n=n, show=True)

