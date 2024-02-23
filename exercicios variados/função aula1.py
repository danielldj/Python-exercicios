def salvar_alunos_em_arquivo(alunos, nome_arquivo):
    with open(nome_arquivo,'w') as arquivo:
        for aluno, info in alunos.items():
            arquivo.write(f'Aluno: {aluno}\n')
            arquivo.write(f'Notas: {", ".join(map(str, info["notas"]))}\n')
            arquivo.write(f'Media: {info["media"]}\n')
            arquivo.write(f'Situacao: {info["situação"]}\n')
            arquivo.write('-' * 20 + '\n')

def exibir_mensagem(texto):
    print('='*len(texto))
    print(texto)
    print('='*len(texto))

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def situação_aluno(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'
    
def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor digite um número inteiro.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n
    
def leiaFloat(texto):
    while True:
        try:
            n = float(input(texto))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor digite um número válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def main():
    exibir_mensagem('Programa de notas dos Alunos')
    alunos = {}
    while True:
        opcao = input('Digite "cadastrar" para cadastrar um aluno ou "sair" para sair do Programa ou "salvar para salvar o programa": ')
        if opcao.lower() == 'sair':
            break
        elif opcao.lower() == 'salvar':
            nome_arquivo = input('Digite o nome do arquivo para salvar os alunos')
            salvar_alunos_em_arquivo(alunos, nome_arquivo)
            print(f'Os dados dos alunos foram salvos em {nome_arquivo}')
            continue
        if opcao.lower() != 'cadastrar':
            print('Opção Invalida Digite "cadastar" ou "sair".')
            continue
        nome_aluno = input(f'Digite o nome do aluno: ')
        notas_alunos = []
        numero_notas = leiaInt(f'Digite quantas notas para o aluno {nome_aluno}: ')
        for c in range(numero_notas):
            notas = leiaFloat(f'Digite a {c+1}° nota do aluno {nome_aluno}: ')
            notas_alunos.append(notas)
        media_alunos = calcular_media(notas_alunos)
        situação = situação_aluno(media_alunos)
        alunos[nome_aluno] = {'notas': notas_alunos, 'media': media_alunos, 'situação': situação}
        
        
    exibir_mensagem('Relatorio dos Alunos:')
    for aluno, info in alunos.items():
        print(f'Aluno: {aluno}')
        print(f'Notas: {info["notas"]}')
        print(f'Media: {info["media"]:.2f}')
        print(f'Situação: {info["situação"]}')
        print('-'*20)
        
    print('Fim do Programa!')
if __name__ == "__main__":
    main()