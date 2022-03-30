'''
1ª questão
Faça um programa que leia da entrada padrão linhas até que uma vazia seja digitada. Para cada linha lida, exceto a vazia, suponha que seja um número inteiro maior que zero. Suponha que este número inteiro é o valor a ser trocado em um número mínimo de cédulas
e/ou moeda. As cédulas possuem valor: 100, 50, 20, 10, 5, 2 reais e a moeda seja de 1 real. Veja o teste a seguir e obedeça rigidamente as escritas na saída padrão, considerando singular ou plural de notas em cada caso, bem como a devida tabulação.

Entradas: 
100
20
8


Saídas Correspondentes:
Trocando 100 em:
   1 nota de 100 reais

Trocando 20 em:
   1 nota de 20 reais

Trocando 8 em:
   1 nota de 5 reais
   1 nota de 2 reais
   1 moeda de 1 real

'''

valores = input()
while valores != '':
    trocar = int(valores)
    n100 = trocar // 100
    sobram = trocar % 100
    n50 = sobram // 50
    sobram = sobram % 50
    n20 = sobram // 20
    sobram = sobram % 20
    n10 = sobram // 10
    sobram = sobram % 10
    n5 = sobram // 5
    sobram = sobram % 5
    n2 = sobram // 2
    sobram = sobram % 2
    n1 = sobram // 1

    print(f'Trocando {trocar} em:')
    if n100 > 1:
        print(f'{n100: >4} notas de 100 reais')
    elif n100 == 1:
        print(f'{n100: >4} nota de 100 reais')
    if n50 > 1:
        print(f'{n50: >4} notas de 50 reais')
    elif n50 == 1:
        print(f'{n50: >4} nota de 50 reais')
    if n20 > 1:
        print(f'{n20: >4} notas de 20 reais')
    elif n20 == 1:
        print(f'{n20: >4} nota de 20 reais')
    if n10 > 1:
        print(f'{n10: >4} notas de 10 reais')
    elif n10 == 1:
        print(f'{n10: >4} nota de 10 reais')
    if n5 > 1:
        print(f'{n5: >4} nota(s) de 5 reais')
    elif n5 == 1:
        print(f'{n5: >4} nota de 5 reais')
    if n2 > 1:
        print(f'{n2: >4} notas de 2 reais')
    elif n2 == 1:
        print(f'{n2: >4} nota de 2 reais')
    if n1 > 1:
        print(f'{n1: >4} moedas de 1 real')
    elif n1 == 1:
        print(f'{n1: >4} moeda de 1 real')
    print()
    valores = input()
