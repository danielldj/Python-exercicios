class Jogador:
    def __init__(self, nome, partidas) -> None:
        self.nome = nome
        self.partidas = partidas
        self.gols = []

    def adicionar_gols(self, gol):
        self.gols.append(gol)

    def media_gols(self):
        return sum(self.gols) / len(self.gols) if self.gols else 0
    

jogadores = {}

continuar = True
while continuar:
    nome_jogador = input('Nome do jogador: ')
    quantidade_partidas = int(input('Quantas partidas: '))

    jogador = Jogador(nome_jogador, quantidade_partidas)

    for c in range(quantidade_partidas):
        gol = int(input(f'Quantos gols na {c+1}° partida: '))
        jogador.adicionar_gols(gol)


    jogadores[nome_jogador] = jogador

    resposta = input('quer continuar[S/N]: ').upper().strip()
    if resposta == 'N':
        continuar = False

print('Relatorio dos Jogadores')

sair = True
while sair:
    relatorio = input('Quer ver o relatório de qual Jogador: ')
    if relatorio in jogadores:
        jogador = jogadores[relatorio]
        print(f'Jogador: {jogador.nome}')
        print(f'Partidas {jogador.partidas}')
        print(f'Gols: {jogador.gols}')
        print(f'Média: {jogador.media_gols():.2f}')
        
    else:
        print(f'O Jogador "{relatorio}" não foi encontrado.')
    
    sair = input('Quer Continuar[S/N]: ').upper().strip()
    if sair == 'N':
        sair = False