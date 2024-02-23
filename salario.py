def calculo_imposto(salário):
    global imposto
    if salario >= 2500:
        imposto = salário * (15/100)
            
    elif salario >= 1101:
        imposto = salário * (10/100)
            
    else:
        imposto = salário * (5/100)
    return imposto       

print('Calculo de salário')
salario = float(input('Digite o salário: '))
beneficio_salario = float(input('Digite os benefecios: '))
calculo_imposto(salario)
total_salario = (salario - imposto ) + beneficio_salario
print(f'O Salário total do funcionario é : {total_salario}')

