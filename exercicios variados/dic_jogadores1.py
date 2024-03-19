jogadores = {}
jogadores['nome'] = input('Digite o nome do Jogador: ')
jogadores['gol']  = []
partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
for p in range(partidas):
    jogadores['gol'].append(int(input(f'Quantos gols na partida {p+1}: ')))
print('=-'*30)

jogadores['Total'] = sum(jogadores['gol'])
print(jogadores)
print('=-'*30)

for j, v in jogadores.items():
    print(f'O campo {j} tem valor {v}.')
print('=-'*30)

print(f'O Jogador {jogadores["nome"]} jogou {partidas} partidas.')
for p, v in enumerate(jogadores['gol']):
    print(f'=> Na Partida {p} Fez {v} gols.')
print(f'Foi um total de {jogadores["Total"]} gols.')