from time import sleep
print('\tMenu de opção para efetuar\n\toperação entre dois números')
n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo  numero '))
opcao = 0
while opcao != 5: 
    print(''' Menu de opção
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Digitar outro numero
          [5] Sair do programa''')
    opcao = int(input('Qual sua opção? '))
    if opcao ==1:
        soma = n1 + n2
        print(f'O valor da soma entre {n1} + {n2} = {soma} ')
    elif opcao ==2:
        mult = n1 * n2
        print(f'O valor da Multiplicação  entre {n1} * {n2} = {mult} ')
    elif opcao ==3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n1 == n2:
            print(f'Os dois números {n1} e {n2} são iguais {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n2}')
    elif opcao == 4:
        print('Digite os dois números: ')
        n1 = int(input('Digite o primeiro numero '))
        n2 = int(input('Digite o segundo  numero '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Digite um valor valido ')
    print('=-='*10)
    sleep(2)
print('Fim do Programa. Volte Sempre!')