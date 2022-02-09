# https://www.beecrowd.com.br/judge/pt/problems/view/1019

'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
N = int(input())
h = N // 3600
tmin = N % 3600
min = tmin // 60
s = tmin % 60
print('{}:{}:{}'.format(h, min, s))

'''
Usando f-string PYTHON 3.6
print(f'{h}:{min}:{s}')
'''
