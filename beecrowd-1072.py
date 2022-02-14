# https://www.beecrowd.com.br/judge/pt/problems/view/1072

'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
'''

n = int(input())
cont = 0
contin = 0
contout = 0

while cont < n:
    num = int(input())
    if num < 10 or num > 20:
        contout += 1
        cont += 1
    else:
        contin += 1
        cont += 1

print('{} in'.format(contin))
print('{} out'.format(contout))

'''
Usando f-string PYTHON 3.6
print(f'{contin} in')
print(f'{contout} out')
'''
