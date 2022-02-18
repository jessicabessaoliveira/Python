# https://www.beecrowd.com.br/judge/pt/problems/view/1045


numeros = input()
lado = numeros.split()
num1 = float(valor[0])
num2 = float(valor[1])
num3 = float(valor[2])

A = num1
if num2 > num1 and num2 > num3:
    A = num2
    B = num1
    C = num3
    if A >= (B + C):
        print(f'NAO FORMA TRIANGULO')
    elif A**2 == B**2 + C**2:
        print(f'TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print(f'TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print(f'TRIANGULO ACUTANGULO')
if num3 > num1 and num3 > num2:
    A = num3
    B = num1
    C = num2
    if A >= (B + C):
        print(f'NAO FORMA TRIANGULO')
    elif A**2 == B**2 + C**2:
        print(f'TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print(f'TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print(f'TRIANGULO ACUTANGULO')
if A == B == C:
    print(f'TRIANGULO EQUILATERO')
if A == B or A == C or B == C:
    print(f'TRIANGULO ISOSCELES')

