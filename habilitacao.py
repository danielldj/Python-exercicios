import datetime
print('Programa Habilitação')
num_pessoas = int(input('Digite quantas pessoas voce quer saber se podem tirar habilitação: '))
for c in range(num_pessoas):
    nome = input('Digite seu nome: ')
    nascimento = int(input('Digite seu ano de nascimento: '))
    ano = datetime.date.today().year
    idade = ano - nascimento
    if idade >= 18:
        print(f'Você tem {idade} anos e já pode tirar a habilitação.')
    else:
        print(f'Você tem {idade} anos e falta {18 - idade} anos para pode tirar a habilitação.')
