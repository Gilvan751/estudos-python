tot18 = totH = totM20 =  0
while True:
    idade = int(input('idade:  '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo:[M/F]  ')).strip().upper()[0]
        
    if idade >= 18:
        tot18 +=1   
    if sexo == 'M':
        totH +=1
    if sexo == 'F' and idade < 20:
        totM20 +=1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? :[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('\n')
print(f'Pessoas com mais de 18 anos {tot18}.\n ')
print(f'Ao todo temos um total de  {totH} homens cadastrados.\n')
print(f'E temos um  total de {totM20}  mulheres  com menos de 20 anos.\n')

