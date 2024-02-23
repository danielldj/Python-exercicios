def calcular_media_gols(gols, partidas):
    total = sum(gols)
    media = total / partidas
    return media



num_jogadores = int(input('Digite quantos jogadores quer cadastrar: '))
jogadores = {}

for i in range(num_jogadores):
    nome_jogador = str(input(f'Digite o nome do {i+1}° jogador: '))
    gols_jogador = []
    num_jogos = int(input(f'Quantos jogos para o jogador {nome_jogador}: '))
    
    for j in range(num_jogos):
        gols = int(input(f'Quantos gols o jogador {nome_jogador} fez na {j+1}° partida: '))
        gols_jogador.append(gols)
        
    
    media_gols =  calcular_media_gols(gols_jogador, num_jogos)
    jogadores[nome_jogador] = {'partidas': num_jogos, 'gols': gols_jogador, 'média-gols/partida': media_gols}
print('Relatorio das Partidas')
for jogador, info in jogadores.items():
    print(f'Jogador {jogador}')
    print(f'Partidas: {info["partidas"]}')
    print(f'Gols: {info["gols"]}')
    print(f'Media de gols / Partida: {info["média-gols/partida"]:.2f}')
    print('-'*20)
