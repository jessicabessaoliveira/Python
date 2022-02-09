# https://www.beecrowd.com.br/judge/pt/problems/view/1020

'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''
idade = int(input())
ano = idade // 365
mes = (idade % 365) // 30
dias = ((idade % 365) % 30)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))

'''
Usando f-string PYTHON 3.6
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
'''
