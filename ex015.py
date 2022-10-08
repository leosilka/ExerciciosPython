print('='*7, ' EXERCICIOS 015 ', '='*7)
print('_'*5, 'Locadora do Léo', '_'*5)
print('| Diaria: R$60,00')
print('| KM Rodado: R$0,15')
print('_'*27)
print('')
diaria = float(input('Informe quantos dias ficou com o carro: '))
vdiaria = diaria * 60
km = float(input('Informe quantos KM rodado com o carro: '))
vkm = km * 0.15
vtotal = vkm + vdiaria
print('Você irá pagar o valor de R${:.2f} pela diaria do carro e irá pagar o valor de R${:.2f} pelo KM rodado. Dando um total de R${:.2f}' .format(vdiaria, vkm, vtotal))
print('')
print('-'*5, 'DEMONSTRATIVO', '-'*5)
print('TOTAL DIARIA: R${:.2f}' .format(vdiaria))
print('TOTAL KM RODADO: R${:.2f}' .format(vkm))
print('')
print('TOTAL: R${:.2f}' .format(vtotal))
print('-'*25)
print('')
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #