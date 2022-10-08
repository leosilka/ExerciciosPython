import random
print('======== EXERCICIO 019 ========')
nprof = input('Prezado(a) Professor(a), informe seu nome: ')
print('Professor(a) {}, informe na sequencia abaixo o nome dos alunos que deseja sortear. ' .format(nprof))
print('')
al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
print('Os nomes dos alunos fornecidos sao: {}, {}, {} e {}' .format(al1, al2, al3, al4))
print('')
nomes = [al1, al2, al3, al4]
def selectRandom(nomes):
    return random.choice(nomes)
print('O aluno selecionado foi: ', selectRandom(nomes))
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #