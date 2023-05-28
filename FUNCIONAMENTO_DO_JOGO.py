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

def dec(txt):
  print()
  print('--'*27)
  print('=='*10,txt,'=='*10)
  print('--'*27)
  print()
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

num=int(input('\033[1;35m>>>\033[mEscolha um numero de 0 á 3: '))
print('\n','--'*27)
if num == 0:
  print('\n\033[1;35m>>>\033[m','A cor que você escolheu foi: \033[1;32mVERDE\033[m\n')
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
