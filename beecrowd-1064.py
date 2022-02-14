# https://www.beecrowd.com.br/judge/pt/problems/view/1064

'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''

cont = 0
soma = 0
for n in range(6):
    num = float(input())
    if (num > 0.0):
        cont += 1
        soma += num
media = soma/cont
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))

'''
Usando f-string PYTHON 3.6
print(f'{cont} valores positivos')
print(f'{media:.1f}')
'''
