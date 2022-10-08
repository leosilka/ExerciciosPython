import random
import time
print('='*7, ' EXERCICIOS 028 v1.0 ', '='*7)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
nsorteado = random.randint(0, 5) #aqui o computador vai pensar no número
ninformado = int(input('Em que número eu pensei? ')) #aqui o jogador vai tentar adivinhar
print('Processando...')
sleep(3)
if ninformado == nsorteado:
    print('Parabéns, você acertou o número que pensei!')
else:
    print('ERROU! Você não acertou o número que pensei que foi {}' .format(nsorteado))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #