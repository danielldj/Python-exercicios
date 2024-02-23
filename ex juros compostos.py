def investimento(inicial, juros, tempo):
    valor_final = inicial * (juros+1)** tempo
    return valor_final


valorinicial = int(input('valor inicial:'))
taxaJuros = float(input('taxa de juros: '))
anos = int(input('anos: '))

valorFinal = investimento(valorinicial, taxaJuros, anos)
print(f'{valorFinal:.2f}')
