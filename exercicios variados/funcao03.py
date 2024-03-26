import datetime
ano = datetime.date.today().year
def voto(nascimento):
    idade = ano - nascimento
    if idade <  18 or idade >= 65:
        return print(f'Idade igual a: {idade} voto OPCIONAL')
    else:
        return print(f'Idade igual a: {idade} voto OBRIGATORIO')



ano_nascimento = int(input('Digite o ano de nascimento: '))

voto(ano_nascimento)
