print('='*7, "EXERCICIOS 022", '='*7)
nome = str(input('Por favor, informe seu nome completo por gentileza: '))
nlista = nome.split()
njuncao = ''.join(nlista)
pnome = nlista[0]
print('')
print('Seu nome', nome, 'com todas as letras maísculas ficará assim >> ', nome.upper())
print('Seu nome', nome, 'com todas as letras minusculas ficará assim >> ', nome.lower())
print('Seu nome possui a quantidade de', len(njuncao), 'letras.')
print('O seu primeiro nome possui a quatidade de ', len(pnome), 'letras.')
print('='*30)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #