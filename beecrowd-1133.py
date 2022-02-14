# https://www.beecrowd.com.br/judge/pt/problems/view/1133

'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.
'''

inicio = int(input())
fim = int(input())
temp = 0
if fim < inicio:
    temp = inicio
    inicio = fim
    fim = temp

for x in range(inicio + 1, fim):
    if x % 5 == 2:
        print(x)
    elif x % 5 == 3:
        print(x)
