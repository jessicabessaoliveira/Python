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

if num2 < num1 and num2 < num3:
    menor = num2
    if num1 < num3:
        maior = num3
        print(f'{num2}')
        print(f'{num1}')
        print(f'{num3}')
    elif num3 < num1:
        menor = num1
        print(f'{num2}')
        print(f'{num3}')
        print(f'{num1}')
if num3 < num1 and num3 < num2:
    menor = num3
    if num1 < num2:
        maior = num2
        print(f'{num3}')
        print(f'{num1}')
        print(f'{num2}')
    elif num2 < num1:
        maior = num1
        print(f'{num3}')
        print(f'{num2}')
        print(f'{num1}')

if num2 > num1 and num2 > num3:
    maior = num2
    if num3 > num1:
        menor = num1
        print(f'{num1}')
        print(f'{num3}')
        print(f'{num2}')
elif num3 > num1 and num3 > num2:
    maior = num3
    if num2 > num1:
        menor = num1
        print(f'{num1}')
        print(f'{num2}')
        print(f'{num3}')
print()
print(f'{num1}')
print(f'{num2}')
print(f'{num3}')
