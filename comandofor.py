soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  # cont +=1
        soma = soma + c  # soma +=c
print('A SOMA DE TODOS {}  VALORES SOLICITADOE É {}'.format(cont, soma))
