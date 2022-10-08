print('======== EXERCICIO 012 ========')
vproduto = float(input('Qual o valor do produto? R$'))
#vdesconto = float(input('Qual a porcentagem de desconto recebido? '))
vdesconto = vproduto * 0.05
vfinal = vproduto - vdesconto
print('')
print('O produto que custava R${:.2f}, na promocao com desconto de 5%, vai custar R${:.2f}' .format(vproduto, vfinal))
print('-'*40)
print('| Valor do produto: R${:.2f}' .format(vproduto))
print('| Valor do desconto recebido: R${:.2f}' .format(vdesconto))
print('| Valor final do produto: R${:.2f}' .format(vfinal))
print('-'*40)
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #