print('='*7, ' EXERCICIOS 029 ', '='*7)
print('_-_'*20)
print(' '*15, 'RADAR ELETRÔNICO')
print('_-_'*20)
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    vmulta = (velocidade - 80) * 7
    print('Cara, cuidado com essa velocidade, você foi multado em R${:.2f} por andar acima de 80Km/H.' .format(vmulta))
else:
    print('Maravilha, você está dentro do limite de velocidade.')
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #