# https://www.beecrowd.com.br/judge/pt/problems/view/1117

'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.
'''

nota_valida = 0
nota = 0
media = 0
while nota_valida != 2:
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        media += nota / 2
        nota_valida += 1
    else:
        print('nota invalida')
print('media = {}'.format(media))

'''
Usando f-string PYTHON 3.6
print(f'media = {media}')
'''
