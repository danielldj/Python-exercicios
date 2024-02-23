import random
def contar_ocorrencia(jogos, lados_dado):
    contadores = {i: 0 for i in range(1, lados_dado + 1)}
    numeros_dado = []

    for _ in range(jogos):
        dado = random.randint(1, lados_dado)
        contadores[dado] += 1
        numeros_dado.append(dado)

    return contadores, numeros_dado


while True:
    try:
        lados_dado = int(input('Digite o quantos lados seu dado vai ter: '))
        jogos = int(input('Digite quantas vezes vai lançar o dado: '))
        contadores , numeros_dado = contar_ocorrencia(jogos, lados_dado)
        print(f'Os {jogos} dados lançados foram {numeros_dado}')
        for numero, contagem in contadores.items():
            print(f'foram {contagem} o valor {numero}')


        continuar = input('Deseja jogar novamente[S/N]: ').strip()[0].upper()
        if continuar not in ['S', 'N']:
            raise ValueError("Por favor, digite 'S' para continuar ou 'N' para sair.")
        if continuar != 'S':
            break
    except ValueError as e:
        print(e)
    except ValueError:
        print("Por favor, digite um número inteiro válido para o número de lados do dado e para o número de Jogos.")