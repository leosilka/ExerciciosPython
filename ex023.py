print('='*7, "EXERCICIOS 023", '='*7)
num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('')
print('-'*15)
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena {}' .format(c))
print('Milhar: {}' .format(m))
print('-'*15)
print('='*30)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #