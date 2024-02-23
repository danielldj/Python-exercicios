def calcular_medias(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


def calcular_situacao(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'
    


num_alunos = int(input('Digite quantos alunos deseja registrar: '))
alunos = {}

for i in range(num_alunos):
    nome_aluno = str(input(f'Digite o nome do aluno {i + 1}: '))
    notas_alunos = []
    
    num_notas = int(input(f'Quantas notas para o aluno {nome_aluno}: '))
    for j in range(num_notas):
        nota = float(input(f'Digite a {j + 1} nota do {nome_aluno}: '))
        notas_alunos.append(nota)
    
    media_aluno = calcular_medias(notas_alunos)
    situacao = calcular_situacao(media_aluno)
    alunos[nome_aluno] = {'notas': notas_alunos, 'media': media_aluno, 'situaçao': situacao}
print('\nRelatorio de Alunos:')
for aluno, info in alunos.items():
    print(f'Aluno: {aluno}')
    print(f'Notas: {info["notas"]}')
    print(f'Médias: {info["media"]:.2f}')
    print(f'Situação: {info["situaçao"]}')
    print('-'*20)

