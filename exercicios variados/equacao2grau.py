import math
print('=+'*10)
print('Equação do 2° grau')
print('=+'*10)

a = int(input('Digite o valor de a: '))
b  = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = b*b -(4*a*c)

print(f'valor de delta é igual a: {delta}')
if delta > 0 or delta  == 0:
    x1 = (-b) + math.sqrt(delta) / (2 * a)
    x2  = (-b) - math.sqrt(delta) / (2 * a)
    print(f'As raizes da equação são: {x1, x2}')
else:
    print('Não existe raizes negativas nos números Racionais')

