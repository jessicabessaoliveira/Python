# https://www.beecrowd.com.br/judge/pt/problems/view/1048
'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	                Percentual de Reajuste
0 - 400.00                  15%
400.01 - 800.00             12%
800.01 - 1200.00            10%
1200.01 - 2000.00           7%
Acima de 2000.00            4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada              	Exemplo de Saída
400.00                                  Novo salario: 460.00
                                        Reajuste ganho: 60.00
                                        Em percentual: 15 %

800.01                                  Novo salario: 880.01
                                        Reajuste ganho: 80.00
                                        Em percentual: 10 %

2000.00                                 Novo salario: 2140.00
                                        Reajuste ganho: 140.00
                                        Em percentual: 7 %

'''
salarioReajustado = 0.0
salario = float(input())
if 0 < salario <= 400.00:
    percentual = 15
    salarioReajustado = salario * (percentual/100) + salario
    reajusteGanho = salarioReajustado - salario
elif 400.01 <= salario <= 800.00:
    percentual = 12
    salarioReajustado = salario * (percentual/100) + salario
    reajusteGanho = salarioReajustado - salario

elif 800.01 <= salario <= 1200.00:
    percentual = 10
    salarioReajustado = salario * (percentual/100) + salario
    reajusteGanho = salarioReajustado - salario

elif 1200.01 <= salario <= 2000.00:
    percentual = 7
    salarioReajustado = salario * (percentual/100) + salario
    reajusteGanho = salarioReajustado - salario

elif salario > 2000.00:
    percentual = 4
    salarioReajustado = salario * (percentual/100) + salario
    reajusteGanho = salarioReajustado - salario

print(f'Novo salario: {salarioReajustado:.2f}')
print(f'Reajuste ganho: {reajusteGanho:.2f}')
print(f'Em percentual: {percentual} %')
