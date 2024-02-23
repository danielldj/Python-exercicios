funcionarios = {'1': input('funcionario 1: '), '2': input('funcionario 2: '),
'3': input('funcionario 3: ')}
print(f'Funcionarios: {funcionarios}')
numero = input('Digite o número correspondente da pessoa que você desja demitir: ')
if numero in funcionarios:
    del(funcionarios[numero])
print(f'Funcionarios restantes: {funcionarios}')
