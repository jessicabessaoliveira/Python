# https://www.beecrowd.com.br/judge/pt/problems/view/1045

'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.
'''

numeros = input()
lado = numeros.split()
num1 = float(lado[0])
num2 = float(lado[1])
num3 = float(lado[2])
A = num1
B = 0
C = 0
if num2 > num1 and num2 > num3:
    A = num2 #lado maior
    B = num1
    C = num3
    if A >= (B + C):
        print(f'NAO FORMA TRIANGULO')
    elif A**2 == B**2 + C**2:
        print(f'TRIANGULO RETANGULO')
        if A == B == C:
            print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
    elif A**2 > B**2 + C**2:
        print(f'TRIANGULO OBTUSANGULO')
        if A == B == C:
            print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
    elif A**2 < B**2 + C**2:
        print(f'TRIANGULO ACUTANGULO')
        if A == B == C:
            print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
if num3 >= num1 and num3 >= num2:
    A = num3 #lado maior
    B = num1
    C = num2
    if A >= (B + C):
        print(f'NAO FORMA TRIANGULO')
    elif A**2 == B**2 + C**2:
        print(f'TRIANGULO RETANGULO')
        if A == B == C:
         print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
    elif A**2 > B**2 + C**2:
        print(f'TRIANGULO OBTUSANGULO')
        if A == B == C:
         print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
    elif A**2 < B**2 + C**2:
        print(f'TRIANGULO ACUTANGULO')
        if A == B == C:
            print(f'TRIANGULO EQUILATERO')
        elif A == B or A == C or B == C:
            print(f'TRIANGULO ISOSCELES')
