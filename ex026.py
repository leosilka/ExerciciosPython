print('='*7, ' EXERCICIOS 026 ', '='*7)
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('A')+1))
print('A última letra A apareceu na posição {}' .format(frase.rfind('A')+1))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #