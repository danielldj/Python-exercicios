import time
def area(largura, altura):
    area = largura * altura
    print(f'A area do seu terreno de {largura} x {altura} terreno é igual a : {area} m²')

larg = float(input('Qual a largura do terreno(m): '))
alt = float(input('Qual a altura do terreno(m): '))
print('Controle de terrenos')
print('='*30)
area(largura=larg, altura=alt)


def linha(msg):
    print('='* len(msg))
    print(msg)
    print('='* len(msg))

linha('Daniel')
linha('vasco')
linha('Vamos ser campeão')


def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p} ')

    if p < 0:
        p *= -1

    if p == 0:
        p == 1

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
    print('Fim!')

contador(0,10,1)
contador(10,0,2)

inicio = int(input('Digite o inicio: '))
passo = int(input('Digite o passo: '))
fim = int(input('Digite fim: '))

contador(inicio, fim, passo)