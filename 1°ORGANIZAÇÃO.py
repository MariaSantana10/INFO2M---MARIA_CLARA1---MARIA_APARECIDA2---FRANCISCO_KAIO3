def dec(txt):
  print()
  print('--'*27)
  print('=='*10,txt,'=='*10)
  print('--'*27)
  print()
def tempo():
  print('\nPROCESSANDO...\n')
  sleep(5)
from time import sleep

dec('\033[0;37;41mJOGO DA FORCA\033[m')
user=str(input('Bem-vindo(a)!\n \nAntes de iniciarmos me diga o seu nome: '))
print('\nOlá, {}{}{}! Eu vou ser o seu guia de jogo!'.format('\033[4;34m',user.capitalize(),'\033[m'))
tempo()

dec('\033[4;31mCOMO FUNCIONA\033[m')

print('-Você vai escolher um numero de 0 á 3;\n \n-Cada número representa uma cor;\n \n-Você vai receber o nome da cor que vc escolheu;\n \n-Em seguida uma palavra MISTERIOSA + UMA DICA sobre ela.\n')
ok1=(input('\033[1;33m---Digite OK para continuar: \033[m'))
tempo()

dec('\033[4;31mREGRAS DO JOGO\033[m')
print('1º Regra:\n \n-Você receberá a quantidade letras presentes na palavra;\n \n2º Regra:\n \n-Você terá 5 tentativas para acertar a palavra;\n \n3º Regra:\n \n-Você terá 3 chances de erro;\n \n4º Regra:\n \n- Na sua última chance de erro,você receberá a ultima dica\n')

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