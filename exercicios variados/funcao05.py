def jogador(jogador='desconhecido', gols=0):
    print(f'O Jogador {jogador} fez {gols} gols no campeonato.')

nome = input('Digote o nome do Jogador: ')
gol = (input('digte o numero de gol(s): '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    jogador(gols=gol)
else:
    jogador(nome, gol)