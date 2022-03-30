'''
2ª Qustão
Faça um programa que leia na primeira linha da entrada padrão a quantidade de testes, chamada aqui de qtdTestes, a serem lidos oportunamente. Na segunda linha é lida a quantidade de valores de cada teste, chamada aqui de qtdValoresTeste. Na terceira linha
um valor mínimo de um intervalo de valores que serão classificados os valores de cada teste. Na quarta linha é lido o valor máximo do intervalo de classificação. Nas linhas seguintes os valores de cada teste devem ser lido. Classifique os valores de cada teste e
escreva na saída padrão quantos valores ficam abaixo do mínimo, quantos ficam dentro do intervalo e quantos ficam acima do máximo. Além disso, escreva também a soma dos valores dentro do intervalo. Siga rigidamente a formatação das escritas na saída padrão.

Entradas: 
2
6
2.5
4.9
1
2
3
4
5
6
2.1
10.8
5.33
4.1
-1.9
7.2

Saídas Correspondentes:
Teste 1:
   Intervalo: [2.5, 4.9]
   Abaixo do Intervalo: 2, No Intervalo: 2,
   Acima do Intervalo: 2.
   Soma dos Valores Dentro do Intervalo: 7.0

Teste 2:
   Intervalo: [2.5, 4.9]
   Abaixo do Intervalo: 2, No Intervalo: 1,
   Acima do Intervalo: 3.
   Soma de Valores no Intervalo: 4.1

'''

qtdTestes = int(input())
qtdValoresTeste = int(input())
valorMin = float(input())
valorMax = float(input())

for i in range(1, qtdTestes + 1):
    cont = 0
    valoresAbaixo = 0
    valoresDentro = 0
    valoresAcima = 0
    somaDentro = 0
    while cont != qtdValoresTeste:
        valoresTeste = float(input())
        if valoresTeste < valorMin:
            valoresAbaixo += 1
        elif valoresTeste >= valorMin and valoresTeste <= valorMax:
            valoresDentro += 1
            somaDentro += valoresTeste
        else:
            valoresAcima += 1
        cont += 1
    tab = ''
    print(f'Teste {i}:')
    print(f'{tab: >3}Intervalo: [{valorMin}, {valorMax}]')
    print(f'{tab: >3}Abaixo do intervalo: {valoresAbaixo},', end=' ')
    print(f'No Intervalo: {valoresDentro}, ', end='')
    print(f'Acima do intervalo: {valoresAcima}.')
    print(f'{tab: >3}Soma dos Valores Dentro do Intervalo: {somaDentro}')
    print()
