def calcular_medias(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


alunos = {}
num_aluno = int(input('Quantos alunos quer cadastrar: '))
for c in range(num_aluno):
    nome_aluno = input('Digite o nome do aluno: ')
    notas_alunos = []

    num_notas = int(input(f'Quantas notas para o aluno{nome_aluno}: '))
    for d in range(num_notas):
        notas = float(input(f'Digite a {d+1}° nota do aluno {nome_aluno}: '))
        notas_alunos.append(notas)
        media_alunos = calcular_medias(notas_alunos)
        alunos[nome_aluno] = {'notas': notas_alunos, 'media': media_alunos}

print('Relatorio dos Alunos:')
for aluno, info in alunos.items():
    print(f'Aluno : {aluno}')
    print(f'Notas: {info["notas"]}')
    print(f'Médias: {info["media"]}')
    print('-'*20)