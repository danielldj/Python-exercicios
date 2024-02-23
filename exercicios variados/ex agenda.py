print('-'*20)
print('Agenda')
print('-'*20)
agenda = {}
agenda_menor18 = {}
numero_pessoas = int(input('Quantas pessoas deseja adicionar a agenda: '))
for c in range(1, numero_pessoas+1):
    nome = input('nome: ')
    cpf = input('CPF: ')
    idade = int(input('Idade: '))
    telefone = int(input('Telefone: '))
    if  idade < 18:
        agenda_menor18[nome] = {'cpf': cpf, 'idade': idade, 'telefone': telefone}
    else:
        agenda[nome] = {'cpf': cpf, 'idade': idade, 'telefone': telefone}
print('-'*20)
print('\nLista de Pessoas:')
print('-'*20)
for pessoa, info in agenda.items():
    print(f'Nome: {pessoa}')
    print(f'CPF: {info["cpf"]}')
    print(f'Idade: {info["idade"]}')
    print(f'Telefone: {info["telefone"]}')
    print('-'*20)

print('-'*20)
print('\nLista de Pessoas com menos de 18 anos:')
for pessoa, info in agenda_menor18.items():
    print(f'Nome: {pessoa}')
    print(f'CPF: {info["cpf"]}')
    print(f'Idade: {info["idade"]}')
    print(f'Telefone: {info["telefone"]}')
    print('-'*20)