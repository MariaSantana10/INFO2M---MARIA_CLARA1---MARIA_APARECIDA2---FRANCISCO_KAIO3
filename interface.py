import pygame as pg
import random 

pg.init()
branco = (255,255,255)
preto = (0,0,0)
screen = pg.display.set_mode((1000,600))

pg.font.init()

font = pg.font.SysFont("courier now", 50)
font_rb = pg.font.SysFont('courier now', 50)
palavras = ['macaco',
            'meritocracia',
            'abacate',
            'antares',
            'ornintorrinco',
            'pão de queijo']
tentativas_de_letras = ['', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ''
click_last_status = False

def desenho_forca(screen,chance):
  pg.draw.rect(screen, branco,(0, 0, 1000, 600))
  pg.draw.line(screen, preto,(100, 500), (100,100),10)
  pg.draw.line(screen, preto,(50, 500), (150,500),10)
  pg.draw.line(screen, preto,(100, 100), (300,100),10)
  pg.draw.line(screen, preto,(300, 100), (300,150),10)
  if chance >= 1:
    pg.draw.circle(screen, preto,(300, 200), 50, 10)
  if chance >=2:
    pg.draw.line(screen, preto,(300,250),(300,350),10)
  if chance >=3:
    pg.draw.line(screen, preto,(300,260),(225,350),10)
  if chance >=4:
     pg.draw.line(screen, preto,(300,260),(375,350),10)
  if chance >=5:
     pg.draw.line(screen, preto,(300,350),(350,450),10)
  if chance >= 6:
     pg.draw.line(screen, preto,(300,350),(250,450),10)

def desenho_restart_botton(screen):
  pg.draw.rect(screen, preto,(700, 100, 200, 65))
  texto = font_rb.render('Recomeçar',True,branco)
  screen.blit(texto,(715, 115))

def sorteando_palavra(palavras,palavra_escolhida,end_game):
  if end_game == True:
    palavra_n = random.radint(0, len(palavras) == 1)
    palavra_escolhida(palavra)



  
while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      quit()
    if event.type == pg.KEYDOWN:
      letra = str(pg.key.name(event.key)).upper()
      print(letra)

    #jogo
    desenho_forca(screen,4)
    desenho_restart_botton(screen)
    pg.display.update()
