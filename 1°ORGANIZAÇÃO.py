def dec():
  print()
  print('--'*27)
  print()
dec()
print('=='*10,'\033[0;30;41mJOGO DA FORCA\033[m','=='*10)
dec()
user=str(input('Bem-vindo(a)!\n \nAntes de iniarmos me diga o seu nome: '))
print('Olá,{}{}{}!\nEu vou ser o seu guia de jogo!'.format('\033[4;34m',user.capitalize(),'\033[m'))
'''
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
'''