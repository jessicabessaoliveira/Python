# https://www.beecrowd.com.br/judge/pt/problems/view/1151

'''
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.
'''

n = int(input())
termo1 = 0
termo2 = 1
if (n == 0):
    print(f'{termo1}')
elif (n == 2):
    print(f'{termo1} {termo2}')
else:
    cont = 3
    print(f'{termo1} {termo2}', end=' ')
    while cont <= n-1: # Foi usado n-1 no laço para que o último termo fosse exibido sem espaço ao final.
        termo3 = termo1 + termo2
        print(f'{termo3}', end=' ')
        termo1 = termo2
        ultimoTermo = termo2 + termo3
        termo2 = termo3
        cont += 1    
    print(f'{ultimoTermo}') 
