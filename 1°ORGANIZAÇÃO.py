from random import choice # da boblioteca de random import apenas o choice
cores = ['vermelho' ,'azul','verde','amarelo']
verde = ['folha','grama','lagarta','gafanhoto']
vermelho = ['morango','tomate','cereja','flor']
amarelo = ['girassol','sol','banana','mel']
azul = ['mirtilo','oceano','borboleta','flor']
verde = choice(verde)#não precisa do random pq já especificamos que dessa biblioteca só vamos usar o choice
vermelho = choice(vermelho)
amarelo = choice(amarelo)
azul = choice(azul)
print (azul)
print(amarelo)
print(vermelho)
print(verde)

#ainda vou organizar o resto
#num = int(input('escreva um ou zero  '))
#if num == 0:
 # print(vermelho)
#if num == 1 :
 # print(azul)