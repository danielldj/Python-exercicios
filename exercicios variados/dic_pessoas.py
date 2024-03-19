pessoas = []
continuar = True

idades = []

while continuar:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper()
    
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    idades.append(idade)


    resposta = str(input('Quer Continuar? [S/N]: ')).upper()
    if resposta == 'N':
        continuar = False

media = sum(idades)/ len(pessoas)
print(f'O grupo tem {len(pessoas)} pessoas.')
print(f'a média de idades do grupo é igual a {media} ')
print(f'As mulheres cadastradas são:')

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'])

print(f'A lista das pessoas acima da media de idades é igual a:')

for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(pessoa['nome'])