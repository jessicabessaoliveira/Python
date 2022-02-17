# https://www.beecrowd.com.br/judge/pt/problems/view/1071

'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''
num1 = int(input())
num2 = int(input())
somaImpar = 0
fim = 1

# Colocando num1 e num2 em ordem crescente
if num2 < num1:
    temp = num2
    num2 = num1
    num1 = temp

while fim != 0:
    if num1 % 2 == 1 and num2 % 2 == 1:
        for i in range(num1+2, num2, 2):
            somaImpar = somaImpar + i
    elif num1 % 2 == 1 and num2 % 2 == 0:
        for i in range(num1+2, num2, 2): # como num1 é ímpar, num1+2 tb é ímpar
            somaImpar = somaImpar + i
    elif num1 % 2 == 0 and num2 % 2 == 0:
        for i in range(num1+1, num2, 2): # como num1 é par num1+1 é ímpar
            somaImpar = somaImpar + i
    elif num1 % 2 == 0 and num2 % 2 == 1:
        for i in range(num1+1, num2, 2):
            somaImpar = somaImpar + i
    print(f'{somaImpar}')
    fim = 0
