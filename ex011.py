print('======== EXERCICIO 011 ========')
largura = float(input('Qual e a largura da parede: '))
altura = float(input('Qual e a altura da parede: '))
dimensao = largura * altura
tinta = 1 * 5
pintura = dimensao / tinta
print('')
print('Sua parede tem a dimensao de {:.0f}m x {:.0f}m e sua area e de {:.0f}m²' .format(largura, altura, dimensao))
print('Para pintar essa parede, você precisará de {}l de tinta' .format(pintura))
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #