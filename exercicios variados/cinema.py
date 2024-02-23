num_filas = 5
num_colunas = 10
acentos_disponiveis = [[True for _ in range(num_colunas)] for _ in range(num_filas)]


def mostar_mapa_acentos():
    print('\nMapa de Acentos')
    print('Legenda: [x]Acento ocupado, [ ]Acento Disponivel')
    print(' ', end='')
    
    for col in range(num_colunas):
        print(f'{col+ 1:2} ', end='')
    print('\n')
    for fila in range(num_filas):
        print(f'{fila+ 1:2} ', end='')
        for col in range(num_colunas):
            if acentos_disponiveis[fila][col]:
                print('[ ]', end=' ')
            else:
                print('[x]', end=' ')
        print()



filmes = {'Vingadores Ultimato': 14.50,
          'Homem-Aranha': 12.50,
          'Rei Leão': 10.00,
          'Jurassic Park':  11.00,
          'A Freira': 13.50}

print('Bem vindo ao Cinema Master!')
print()
print('Filmes Disponiveis: ')
print()
for filme, preço in filmes.items():
    print(f'{filme} - Preço: R${preço:.2f}')

while True:
    filme_escolhido = input('Escolha o filme desejado: ')
    if filme_escolhido in filmes:
        break
    else:
        print('Filme não encontrado! Tente novamente.')

quantidade_de_ingressos = int(input('Quantos ingressos deseja comprar: '))
preco_unitario = filmes[filme_escolhido] 
preco_total = preco_unitario * quantidade_de_ingressos
mostar_mapa_acentos()
print(f'O preço total para {quantidade_de_ingressos} ingressos do filme {filme_escolhido} é R${preco_total:.2f}')







