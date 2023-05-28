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



def mostrar_tamanho(lista):
  print(estado_atual*len(lista))
  print(len(lista))
  print(lista)


def letra_pertence(lista):
  letra=str(input('Digite uma letra: '))
  # while letra in letras_ditas:
  #   print('Você já escolheu essa letra! Tente novamente com outra letra.')
  #   letra=str(input('Digite uma letra: '))   
  letra=letra.upper()
  letras_ditas.append(letra)
          
  if letra in (lista):
    print ('vc acertou!!')
    for t in range(len(lista)):
      if letra == lista[t]:
        estado_atual[t]=letra
  else:
    print('Vc errou')   

  print('Esse é o seu estado atual:')
  print(estado_atual)


num=int(input('Escolha um numero de 0 á 3: '))

if num == 0:
  mostrar_tamanho (verde)
  estado_atual= estado_atual*len(verde)
  while tentativas<chances:
    letra_pertence(verde)
    tentativas+=1
  
    print('As letras q vc já disse foram: ')
  
    for l in letras_ditas:
      print(l, end=' ')
    print('\nvc ja fez',tentativas,'tentativas agr vc tem',chances-tentativas,'tentativas')


if num == 1:
  mostrar_tamanho(vermelho)
  estado_atual= estado_atual*len(vermelho)
  while tentativas<chances:
    letra_pertence(vermelho)
    tentativas+=1
  
    print('As letras q vc já disse foram: ')
  
    for l in letras_ditas:
      print(l, end=' ')
    
    print('\nvc ja fez',tentativas,'tentativas agr vc tem',chances-tentativas,'tentativas')


if num == 2:
  mostrar_tamanho(amarelo)
  estado_atual= estado_atual*len(amarelo)
  while tentativas<chances:
    letra_pertence(amarelo)
    tentativas+=1
  
    print('As letras q vc já disse foram: ')
  
    for l in letras_ditas:
      print(l, end=' ')
    print('\nvc ja fez',tentativas,'tentativas agr vc tem',chances-tentativas,'tentativas')


if num == 3:
  mostrar_tamanho(azul)
  estado_atual= estado_atual*len(azul)
  while tentativas<chances:
    letra_pertence(azul)
    tentativas+=1
  
    print('As letras q vc já disse foram: ')
  
    for l in letras_ditas:
      print(l, end=' ')
    print('\nvc ja fez',tentativas,'tentativas agr vc tem',chances-tentativas,'tentativas')