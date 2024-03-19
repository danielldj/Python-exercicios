continuar = True
jogador = {}

while continuar:

    nome_jogador = str(input('Nome do Jogador: '))
    num_partidas = int(input(f'Digite quantas partidas o jogador {nome_jogador} jogou: '))
    gol = []
    for c in range(num_partidas):
        gol.append(int(input(f'Digite Quantos gols na {c+1}° partida: ')))
    
    media = sum(gol) / num_partidas
    jogador[nome_jogador] = {'gols': gol , 'média': media}

    resposta = input('Quer Continuar [S/N]: ').upper()
    if resposta == 'N':
        continuar = False
print('='*30)
print('Relatorio das Partidas')
for jogadores, info in jogador.items():
    print(f'Jogador {jogadores}     ', end='')
    print(f'Gols: {info["gols"]}'      , end='')
    print(f'      Média: {info["média"]:.2f}')
    print('-'*20)
continuar = True
while continuar:
    dados = input('Mostrar dados de qual jogador: ')
    
    if dados in jogador:  
        gols_do_jogador = jogador[dados]['gols']  
        print(f"Gols do jogador {dados}: {gols_do_jogador}")
    else:
        print(f"O jogador {nome_jogador} não está na lista.")

    resposta = input('Quer Continuar [S/N]: ').upper()
    if resposta == 'N':
        continuar = False