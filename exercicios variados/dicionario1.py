import random
jogadores = {}
jogadores['jogador1'] = random.randint(1, 6)
jogadores['jogador2'] = random.randint(1, 6)
jogadores['jogador3'] = random.randint(1, 6)
jogadores['jogador4'] = random.randint(1, 6)

for j, v in jogadores.items():
    print(f'{j} tirou {v}')

print('Raking dos Jogadores:')
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'1° Lugar {i} tirou {jogadores[i]}')