print('='*7, ' EXERCICIOS 033 ', '='*7)
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('')
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitando foi {}' .format(menor))
print('O maior valor digitado foi {}' .format(maior))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #