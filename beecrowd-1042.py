# https://www.beecrowd.com.br/judge/pt/problems/view/1042

'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

numeros = input()
valor = numeros.split()
num1 = int(valor[0])
num2 = int(valor[1])
num3 = int(valor[2])

n1 = num1
n2 = num2
n3 =num3

# Ordenando num1<num2<num3
if num3 < num2:
    temp = num3
    num3 = num2
    num2 = temp
if num3 < num1:
    temp = num3
    num3 = num1
    num1 = temp
if num2 < num1:
    temp = num2
    num2 = num1
    num1 = temp

print(f'{num1}')
print(f'{num2}')
print(f'{num3}')
print()
print(f'{n1}')
print(f'{n2}')
print(f'{n3}')
