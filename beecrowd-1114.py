# https://www.beecrowd.com.br/judge/pt/problems/view/1114

'''
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.
'''

senha = 1
while senha != 2002:
    senha = int(input())
    if senha == 2002:
        print('Acesso Permitido')
    else:
        print('Senha Invalida')
        