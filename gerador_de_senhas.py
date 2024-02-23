import random
import string
print('Gerador de Senhas')
print('='*20)
numero_senhas = int(input('Quantas senhas você deseja: '))
tamanho_senhas = int(input('Qual o tamanho das senhas: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
for s in range(numero_senhas):
    senhas = ''.join(random.choice(caracteres)for _ in range(tamanho_senhas))
    print(senhas)