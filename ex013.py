print('='*7, ' EXERCICIOS 013 ', '='*7)
nfunc = input('Olá, informe o seu nome: ')
vsal = float(input('Olá {}, me informe o seu salário R$' .format(nfunc)))
porc = int(input('Informe a porcentagem (%) de aumento que recebeu: '))
porc2 = porc * 0.01
vaumento = vsal * porc2
nvsal = vaumento + vsal
print('')
print('{}, seu novo salário será de R${:.2f}.' .format(nfunc, nvsal))
print('{}, você recebeu um aumento de R${:.2f}. Referente a {}% de aumento' .format(nfunc, vaumento, porc))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #