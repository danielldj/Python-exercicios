def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


def condicao(media):
    if media <= 5:
        return 'Reprovado'
    elif media < 7: 
        return 'Recuperação'
    else:
        return 'Aprovado'
    


aluno = {}
continuar = True
while continuar:
    nome_aluno = input('Nome do Aluno: ')
    quantidade_notas = int(input(f'Quantas notas para o aluno {nome_aluno}: '))
    nota = []
    
    for c in range(quantidade_notas):
        nota.append(float(input(f'{c+1}° Nota: ')))
        
    media_alunos = calcular_media(nota)
    aprovacao = condicao(media_alunos)
    aluno[nome_aluno] = {'Notas': nota, 'Media': media_alunos, 'Condição': aprovacao}

    resposta =  input('Quer continuar[S/N]: ').upper().strip()
    if resposta == 'N':
        continuar = False


print('Relatorio Alunos')
sair = True
while sair:
    relatorio = input('Quer ver o relatorio de qual aluno: ')
    if relatorio in aluno:
        aluno_info = aluno[relatorio]
        print(f'Aluno: {relatorio}')
        print(f'Notas: {aluno_info["Notas"]}')
        print(f'Média: {aluno_info["Media"]}')
        print(f'Condição: {aluno_info["Condição"]}')
    else:
        print(f'O aluno "{relatorio}" não foi encontrado.')
    
    sair = input('Quer Continuar[S/N]: ').upper().strip()
    if sair == 'N':
        sair = False