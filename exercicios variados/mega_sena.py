import random
from time import sleep

def gera_jogo():
    mega_sena = []
    while len(mega_sena) < 6:
        numero = random.randint(1,60)
        if numero not in mega_sena:
            mega_sena.append(numero)
    return sorted(mega_sena)

print('======== Jogo da Mega Sena =========')
print()
numero_de_jogos = int(input('Quantos Jogos deseja fazer: '))
print()
sleep(1)
print('Vou Pensar nos melhores números para você!')
print('Gerando....')
sleep(2.5)
for jogo in range(1,numero_de_jogos+1):
    numero_jogos = gera_jogo()
    sleep(0.5)
    print(f'Jogo {jogo}: {numero_jogos}')
print()
sleep(1)
print('Boa sorte! Se vencer não gaste tudo com Doces. rs :)')