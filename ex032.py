from datetime import date #modulo que irá puxar o ano da maquina
print('='*7, ' EXERCICIOS 032 ', '='*7)
ano = int(input('Qual o ano que deseja analisar? Coloque o 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #aqui irá verificar o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #aqui seguirá as regras do ano bissexto
    print('O ano {} é bissexto.' .format(ano))
else:
    print('O ano {} não é bissexto.' .format(ano))
print('='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #