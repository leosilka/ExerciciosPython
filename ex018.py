import math
print('======== EXERCICIO 018 ========')
angulo = float(input('Informe o angulo que voce deseja: '))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('')
print('-'*45)
print('O angulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}' .format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))
print('-'*45)
print('')
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #