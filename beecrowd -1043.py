 # https://www.beecrowd.com.br/judge/pt/problems/view/1043

'''
 Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''
lados = input()
lado = lados.split()
A = float(lado[0])
B = float(lado[1])
C = float(lado[2])

# Ordenando A>B>C
if A < B:
    temp = A
    A = B
    B = temp
elif A < C:
    temp = A
    A = C
    C = temp
elif B < C:
    temp = B
    B = C
    C = temp

if A >= (B + C): #não é um triângulo
    areaTrapezio = ((A  + B) * C)/2
    print(f'Area = {areaTrapezio:.1f}')
else: # é um triângulo A<B+C
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}') 
    