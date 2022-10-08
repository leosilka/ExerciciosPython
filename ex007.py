print('======== EXERCICIO 007 ========')
al = input('Digite o nome do(a) aluno(a): ')
nota1 = float(input('Digite a primeira nota de(a) {}: ' .format(al)))
nota2 = float(input('Digite a segunda nota de(a) {}: ' .format(al)))
print('')
media = (nota1 + nota2) / 2
print('A media do(a) aluno(a) {} foi {:.1f}.' .format(al, media))
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #