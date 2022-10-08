import random
print('======== EXERCICIO 020 ========')
nprof = input('Ola Professor(a), informe seu nome: ')
print('Professor(a) {}, abaixo, crie a lista de 5 alunos que deseja que apresente o trabalho.' .format(nprof))
print('')
al1 = input('Informe o nome do Aluno: ')
al2 = input('Informe o nome do Aluno: ')
al3 = input('Informe o nome do Aluno: ')
al4 = input('Informe o nome do Aluno: ')
al5 = input('Informe o nome do Aluno: ')
print('O nome dos alunos informados foram: {}, {}, {}, {} e {}' .format(al1, al2, al3, al4, al5))
print('')
alunos = [al1, al2, al3, al4, al5]
random.shuffle(alunos)
print('A ordem de apresentacao do trabalho sera: ', alunos)
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #