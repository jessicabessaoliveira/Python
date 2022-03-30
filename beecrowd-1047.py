# https://www.beecrowd.com.br/judge/pt/problems/view/1047

'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''
jogo = input()
tempo = jogo.split()
hInicial = int(tempo[0])
minInicial = int(tempo[1])
hFinal = int(tempo[2])
minFinal = int(tempo[3])
'''
hi = hInicial * 60
inicioJogo = hi + minInicial
hf = hFinal * 60
fimJogo = hf + minFinal

partida = fimJogo - inicioJogo


if partida < 0:
    partida = 1440 + partida

horas = partida // 60
minutos = partida % 60

if hf - hi == 0:
    horas = 24

if partida <= 1440 and partida > 0:
        print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
'''
horaTotal = hFinal - hInicial
minTotal = minFinal - minInicial

if horaTotal < 0:
    horaTotal += 24

if minTotal < 0:
    minTotal += 60
    horaTotal -= 1

if minTotal == 0 and horaTotal == 0:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {horaTotal} HORA(S) E {minTotal} MINUTO(S)')
