def dec(txt):
  print()
  print('--'*27)
  print('=='*10,txt,'=='*10)
  print('--'*27)
  print()
def tempo():
  print('\nPROCESSANDO...\n')
  sleep(3)
from time import sleep

dec('\033[1;30;45mJOGO DA FORCA\033[m')
user=str(input('Bem-vindo(a)!\n \nAntes de iniciarmos, me diga o seu nome: '))
print('\nOlá, {}{}{}! Eu vou ser o seu guia de jogo!'.format('\033[4;35m',user.capitalize(),'\033[m'))
tempo()

dec('\033[4;35mCOMO FUNCIONA\033[m')

print('-Você vai escolher um número de 0 á 3;\n \n-Cada número representa uma cor;\n \n-Você vai receber o nome da cor que vc escolheu;\n \n-Em seguida uma palavra MISTERIOSA + UMA DICA sobre ela.\n')
tempo()

dec('\033[4;35mREGRAS DO JOGO\033[m')
print('1º Regra:\n \n-Você receberá a quantidade letras presentes na palavra;\n \n2º Regra:\n \n-Você terá 8 tentativas para acertar a palavra.')
tempo()

from random import choice

verde = ['folha','grama','lagarta','trevo']
vermelho = ['morango','tomate','cereja','flor']
amarelo = ['estrela','sol','banana','mel']
azul = ['mirtilo','oceano','baleia','flor']

verde = choice(verde).upper()
vermelho = choice(vermelho).upper()
amarelo = choice(amarelo).upper()
azul = choice(azul).upper()

letras_ditas=[]

estado_atual=[' _ ']

tentativas=0

chances=8
def dica0(verdes):
  if verdes[0]:
    print('\n\033[1;35mDICA:\033[m','TEM EM ÁRVORES\n')
  elif verdes[1]:
    print('\n\033[1;35mDICA:\033[m','TEM NO CAMPO; TEM NO QUINTAL DE CASA\n')
  elif verdes[2]:
    print('\n\033[1;35mDICA:\033[m','VIRA BORBOLETA\n')
  elif verdes[3]:
    print('\n\033[1;35mDICA:\033[m','CONHECIDO POR TER 4 FOLHAS.\n')
def dica1(vermelhas):
  if vermelhas[0]:
    print('\n\033[1;35mDICA:\033[m','FRUTA VERMELHA; SABOR DOS BATONS INFANTIS\n')
  elif vermelhas[1]:
    print('\n\033[1;35mDICA:\033[m','CONHECIDO POR SER FRUTA OU VERDURA\n')
  elif vermelhas[2]:
    print('\n\033[1;35mDICA:\033[m','PARECE UMA ACEROLA; DECORAÇÃO DE BOLO\n')
  elif vermelhas[3]:
    print('\n\033[1;35mDICA:\033[m','AS MULHERES GANHAM DOS SEUS COMPANHEIROS EM DATAS ESPECIAIS\n')
def dica2(amarelas):

  if amarelas[0]:
    print('\n\033[1;35mDICA:\033[m','NA VIA LÁCTEA O SOL É CONHECIOD COMO UMA?\n')
  elif amarelas[1]:
    print('\n\033[1;35mDICA:\033[m','NA VIA LÁCTEA É CONHECIDO COMO UMA ESTRELA\n')
  elif amarelas[2]:
    print('\n\033[1;35mDICA:\033[m','COMIDA FAVORITA DOS MINIONS\n')
  elif amarelas[3]:
    print('\n\033[1;35mDICA:\033[m','VEM DAS ABELHAS\n')
def dica3(azuis):
  if azuis[0]:
    print('\n\033[1;35mDICA:\033[m','NOME DE UMA PERSONAGEM DO DESENHO DA MORANGUINHO\n')
  elif azuis[1]:
    print('\n\033[1;35mDICA:\033[m','SÓ 5% FOI EXPLORADO\n')
  elif azuis[2]:
    print('\n\033[1;35mDICA:\033[m','MAIOR ANIMAL QUE EXISTE\n')
  elif azuis[3]:
    print('\n\033[1;35mDICA:\033[m','AS MULHERES GANHAM DOS SEUS COMPANHEIROS EM DATAS ESPECIAIS\n')
def mostrar_tamanho(lista):
  print(estado_atual*len(lista))
  print('\n\033[1;35m>>>\033[m','A palavra misteriosa tem',len(lista),'letras')
  # print(lista)
  print('\n','--'*27)
def letra_pertence(lista):
  letra=str(input('\n\n\033[4;35mDigite uma letra:\033[m '))
  letra=letra.upper()
  while letra in letras_ditas:
    print('\nVOCÊ JÁ ESCOLHEU ESSA LETRA! TENTE NOVAMENTE COM OUTRA LETRA.')
    letra=str(input('\n\n\033[4;35mDigite uma letra:\033[m ')) 
    letra=letra.upper()
  letras_ditas.append(letra)
          
  if letra in (lista):
    print('\n<<< VOCÊ ACERTOU! >>>')
    for t in range(len(lista)):
      if letra == lista[t]:
        estado_atual[t]=letra
  else:
    print('\n<<< OOPS! VOCÊ ERROU! >>>')   

  print('\n\033[1;35m>>>\033[m','Esse é o seu estado atual:\n')
  print(estado_atual)
def final_de_jogo(lista):
  if chances==tentativas:
    print('\n\033[1;35m>>>\033[m','VOCÊ PERDEU!')
    print('\n\033[1;35m>>>\033[m','A PALAVRA CORRETA ERA: ',(lista))
  else:
    print('\n\033[1;35m>>>\033[m','VOCÊ GANHOU!')
dec('\033[4;35mVAMOS COMEÇAR!\033[m')
tempo()
num=int(input('\033[1;35m>>>\033[mEscolha um numero de 0 á 3: '))
print('\n','--'*27)
if num == 0:
  print('\n\033[1;35m>>>\033[m','A cor que você escolheu foi: \033[1;32mVERDE\033[m\n')
  dica0(verdes)
  mostrar_tamanho (verde)
  estado_atual= estado_atual*len(verde)
  while tentativas<chances and ''. join(estado_atual) != verde:
    letra_pertence(verde)
    tentativas+=1

    print('\n\033[1;35m>>>\033[m','As letras que você já disse foram:\n ')
    
    for l in letras_ditas:
      print(l, end=' ')

    print('\n\n\033[1;35m>>>\033[m','VOCÊ JÁ FEZ',tentativas,'TENTATIVAS, AGORA RESTAM',chances-tentativas,'TENTATIVAS')

  final_de_jogo(verde)
if num == 1:
  print('\n\033[1;35m>>>\033[m','A cor que você escolheu foi: \033[1;31mVERMELHO\033[m\n')
  dicas1(vermelhas)
  mostrar_tamanho(vermelho)
  estado_atual= estado_atual*len(vermelho)
  while tentativas<chances and ''. join(estado_atual) != vermelho:
    letra_pertence(vermelho)
    tentativas+=1
  
    print('\n\033[1;35m>>>\033[m','As letras q vc já disse foram:\n ')
  
    for l in letras_ditas:
      print(l, end=' ')
    
    print('\n\n\033[1;35m>>>\033[m','VOCÊ JÁ FEZ',tentativas,'TENTATIVAS, AGORA RESTAM',chances-tentativas,'TENTATIVAS')
  final_de_jogo(vermelho)
if num == 2:
  print('\n\033[1;35m>>>\033[m','A cor que você escolheu foi: \033[1;33mAMARELO\033[m\n')
  dicas2(amarelas)
  mostrar_tamanho(amarelo)
  estado_atual= estado_atual*len(amarelo)
  while tentativas<chances and ''. join(estado_atual) != amarelo:
    letra_pertence(amarelo)
    tentativas+=1
  
    print('\n\033[1;35m>>>\033[m','As letras q vc já disse foram:\n ')
  
    for l in letras_ditas:
      print(l, end=' ')
      
    print('\n\n\033[1;35m>>>\033[m','VOCÊ JÁ FEZ',tentativas,'TENTATIVAS, AGORA RESTAM',chances-tentativas,'TENTATIVAS')
  final_de_jogo(amarelo)
if num == 3:
  print('\n\033[1;35m>>>\033[m','A cor que você escolheu foi: \033[1;36mAZUL\033[m\n')
  dicas3(azuis)
  mostrar_tamanho(azul)
  estado_atual= estado_atual*len(azul)
  while tentativas<chances and ''. join(estado_atual) != azul:
    letra_pertence(azul)
    tentativas+=1
  
    print('\n\033[1;35m>>>\033[m','As letras q vc já disse foram:\n ')
  
    for l in letras_ditas:
      print(l, end=' ')
    print('\n\n\033[1;35m>>>\033[m','VOCÊ JÁ FEZ',tentativas,'TENTATIVAS, AGORA RESTAM',chances-tentativas,'TENTATIVAS')
  final_de_jogo(azul)

