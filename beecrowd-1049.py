# https://www.beecrowd.com.br/judge/pt/problems/view/1049

'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

imagem: 
https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1049_b.png

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

dica1 = input()
dica2 = input()
dica3 = input()
if dica1 == "vertebrado":
    if dica2 == "ave":
        if dica3 == "carnivoro":
            print('aguia')
        elif dica3 == "onivoro":
            print('pomba')
    elif dica2 == "mamifero":
        if dica3 == "onivoro":
            print('homem')
        elif dica3 == "herbivoro":
            print('vaca')
elif dica1 == "invertebrado":
    if dica2 == "inseto":
        if dica3 == "hematofago":
            print('pulga')
        elif dica3 == "herbivoro":
            print('lagarta')
    elif dica2 == "anelideo":
        if dica3 == "hematofago":
            print('sanguessuga')
        elif dica3 == "onivoro":
            print('minhoca')
            