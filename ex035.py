import time
cores = {'limpa': '\033[m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',}
print('\033[1;34m='*7, ' \033[31mEXERCICIOS 035 ', '\033[34m='*7)
print(cores['limpa'])
time.sleep(2)
print('\033[32m-='*30)
print(' '*15, '{}ANALISADOR {}DE {}TRIANGULO' .format(cores['azul'], cores['verde'], cores['vermelho']))
print('\033[32m-='*30)
print(cores['limpa'])
r1 = float(input('Digite o primeiro segmento: '))
time.sleep(1)
r2 = float(input('Digite o segundo segmento: '))
time.sleep(1)
r3 = float(input('Digite o terceiro segmento: '))
print('')
print('{}Processando informacoes...{}' .format(cores['roxo'], cores['limpa']))
time.sleep(5)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODE FORMAR{} triângulo!' .format(cores['azul'], cores['limpa']))
else:
    print('Os segumentos acima {}NÃO PODE FORMAR{} triângulo!' .format(cores['vermelho'], cores['limpa']))
print('\033[1;34m='*32)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #