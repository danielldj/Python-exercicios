def maior(*valores):
     if not valores:
        print("Nenhum valor foi informado.")
     else:
        print('=-'*30)
        print('Analisando os valores passados....')
        print(f'{valores} foram informados {len(valores)} ao todo.')
        print(f'O maior valor informado foi {max(valores)}.')
    

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
