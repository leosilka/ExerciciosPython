import math
print('======== EXERCICIO 017 ========')
coposto = float(input('Qual o comprimento do cateto oposto: '))
cadjacente = float(input('Qual o comprimento do cateto adjacente: '))
poposto = math.pow(coposto, 2)
padjacente = math.pow(cadjacente, 2)
hipotenusa = math.sqrt(poposto + padjacente)
print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #