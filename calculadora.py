def soma(a,b):
    s = a + b
    return s

def subtracao(a,b):
    s = a - b
    return s

def multiplicacao(a,b):
    s = a * b
    return s

def divisao(a,b):
    s = a / b 
    return s


print('Calculadora')
while True:
    print('''
             opção [0]: Soma
             opção [1]: Subtração
             opção [2]: Multiplicação
             opção [3]: Divisão''')
    
    opcao = int(input('Digite a opção desejada: '))
    
    a = float(input('Digite o 1° numero: '))
    b = float(input('Digite o 2° numero: '))
    
    if opcao == 0:
       print(soma(a, b))

    elif opcao == 1:
        print(subtracao(a, b))   
    
    elif opcao == 2:
        print(multiplicacao(a, b))
    
    elif opcao == 3:
        print(divisao(a, b)) 

    else:
        print('Opção Invalida Tente Novamente!')

    continuar = input('Deseja continuar[S/N]: ').strip()[0].upper()
    if continuar == 'N':
        break