print('='*7, ' EXERCICIOS 034 ', '='*7)
print('')
print('-'*30)
print(' '*2,'CALCULADORA DE SALÁRIO')
print('-'*30)
vsal = float(input('Informe o seu salário: R$'))
if vsal > 1250:
    vaumento = vsal * 0.10
    nvsal = vaumento + vsal
    print('O seu novo salário será de R${:.2f}!' .format(nvsal))
    print('Você recebeu um aumento de R${:.2f}, um aumento de 10%!' .format(vaumento))
else:
    vaumento = vsal * 0.15
    nvsal = vaumento + vsal
    print('O seu novo salário será de R${:.2f}!' .format(nvsal))
    print('Você recebeu um aumento de R${:.2f}, um aumento de 15%!' .format(vaumento))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #