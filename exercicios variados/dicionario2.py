import datetime
ano = datetime.date.today().year

funcionario = {}
funcionario['Nome'] = input('Digite o nome: ')
nascimento = int(input('Digite o ano de Nascimento: '))
funcionario['Idade'] = ano - nascimento
funcionario['CTPS'] = int(input('Digite o numero da carteira de trablho (0 para não tem): '))
if funcionario['CTPS'] != 0:
    funcionario['Contratação'] = int(input('Ano de Contratação: '))
    funcionario['Salário'] = int(input('Salário: R$ '))
    funcionario['Aposentadoria'] = funcionario['Contratação'] + 35 - nascimento

for f, v in funcionario.items():
    print(f'{f} tem valor {v}')
