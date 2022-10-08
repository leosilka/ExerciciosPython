print('='*7, ' EXERCICIOS 031 ', '='*7)
print('')
print('_'*30)
print(' '*3, 'RODOVIARIA DE CURITIBA')
print('_'*30)
print('')
print('*'*45)
print('VALORES:')
print('R$0,50 por Km (para viagens de até 200Km).')
print('R$0,45 por Km (para viagens acima de 200Km).')
print('*'*45)
print('')
distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    vdistancia = distancia * 0.50
    print('Você irá viajar {:.2f}Km e irá pagar o valor de R${:.2f}.' .format(distancia, vdistancia))
else:
    vdistancia = distancia * 0.45
    print('Você irá viajar {:.2f}Km e irá pagar o valor de R${:.2f}.' .format(distancia, vdistancia))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #