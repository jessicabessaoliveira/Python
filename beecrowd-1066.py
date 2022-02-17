# https://www.beecrowd.com.br/judge/pt/problems/view/1066

'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

contPos = 0
contNeg = 0
contPar = 0
contImpar = 0

for i in range(1, 6):
    n = int(input())
    if (n % 2 == 0):
        contPar = contPar + 1
        if (n > 0):
            contPos = contPos + 1
        elif (n < 0):
            contNeg = contNeg + 1
    elif (n % 2 != 0):
        contImpar = contImpar + 1
        if (n > 0):
            contPos = contPos + 1
        elif (n < 0):
            contNeg = contNeg + 1
print(f'{contPar} valor(es) par(es)')
print(f'{contImpar} valor(es) impar(es)')
print(f'{contPos} valor(es) positivo(s)')
print(f'{contNeg} valor(es) negativo(s)')
