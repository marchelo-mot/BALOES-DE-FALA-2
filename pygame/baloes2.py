#Título:NOVOS Balões de diálogos e NOVOS personagens
#link do material da aula: https://bit.ly/pythontela01
#programa com modelo dos balões


import pygame
import math

pygame.init()
game_display = pygame.display.set_mode((800 , 600))
pygame.display.set_caption('A Matemática está em tudo')
clock = pygame.time.Clock()   # relogio pra temporizar a animaçao
personagem1 = pygame.image.load('mario.png')
personagem2 = pygame.image.load('luigi.png')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (120, 120)
  
# Scale the image to your needed size
personagem2 = pygame.transform.scale(personagem2, DEFAULT_IMAGE_SIZE)

t=0
x= 100
y = 470
x1 = 0
x2 = 0
a = 300
b = 450
a1 = 0
a2 = 0

def balao(screen,text, x0,y0):
    font = pygame.font.SysFont('comicsansms', 12, bold=False, italic=False)  #pygame.font.Font(font, 12)
    textSurf = font.render(text, True, (30,30,30)).convert_alpha()
    textSize = textSurf.get_size()   
    bubbleSurf = pygame.Surface((textSize[0] + 31, textSize[1] + 15 + 30))
    bubbleSurf.fill((0,0,0))
    bubbleSurf.set_colorkey((0,0,0))  
    l = 6
    x,y = textSize[0] + 30, textSize[1] + 15
    points = [ [l,0], [x-l,0],[x,l],[x,y-l],[x-l,y], [x/2+6,y] ,[x/2,y+30], [x/2-6,y] ,[l,y],[0,y-l],[0,l]]
    pygame.draw.polygon(bubbleSurf, (255,255,255), points)
    pygame.draw.lines(bubbleSurf, (30,30,30), True, points)
    bubbleRect = bubbleSurf.get_rect()
    bubbleSurf.blit(textSurf, textSurf.get_rect(center = (x/2,y/2)))
    bubbleRect.center = (x0,y0-bubbleRect[3]/2)
    screen.blit(bubbleSurf, bubbleRect)
    
def balao2(screen,text, a0,b0):
    font = pygame.font.SysFont('comicsansms', 12, bold=False, italic=False)  #pygame.font.Font(font, 12)
    textSurf = font.render(text, True, (30,30,30)).convert_alpha()
    textSize = textSurf.get_size()   
    bubbleSurf = pygame.Surface((textSize[0] + 31, textSize[1] + 15 + 30))
    bubbleSurf.fill((0,0,0))
    bubbleSurf.set_colorkey((0,0,0))  
    l = 6
    a,b = textSize[0] + 30, textSize[1] + 15
    points = [ [l,0], [a-l,0],[a,l],[a,b-l],[a-l,b], [a/2+6,b] ,[a/2,b+30], [a/2-6,b] ,[l,b],[0,b-l],[0,l]]
    pygame.draw.polygon(bubbleSurf, (255,255,255), points)
    pygame.draw.lines(bubbleSurf, (30,30,30), True, points)
    bubbleRect = bubbleSurf.get_rect()
    bubbleSurf.blit(textSurf, textSurf.get_rect(center = (a/2,b/2)))
    bubbleRect.center = (a0,b0-bubbleRect[3]/2)
    screen.blit(bubbleSurf, bubbleRect)

pygame.font.init()
fs = pygame.font.get_fonts()
print(fs)
itera = 0
itera2 = 0
itera3 = 0
itera4 = 0
itera5 = 0
falas = ["qual é seu nome?"]
falas2 = ["Olá, eu sou o Luigi.", "E o seu?"]
falas3 = ["eu sou o mario"]
falas4 = ["serio?", "que mario?"]
falas5 = ["..."]


while True :
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -2
            if event.key == pygame.K_RIGHT:
                x2 = +2
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a1 = 0
            if event.key == pygame.K_d:
                a2 = 0
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a1 = -2
            if event.key == pygame.K_d:
                a2 = +2
        x += x1 + x2
        a += a1 + a2
        game_display.fill((135,206,235))
        game_display.blit(personagem1, (x, y))
        game_display.blit(personagem2, (a, b))
        if itera<90:
         tx,ty = x+25,y-2
         itera2 = 0
         itera3 = 0
         itera4 = 0 
         itera5 = 0
         balao(game_display,falas[int(itera/90)%len(falas)],tx,ty)
        if itera2>1 and itera2<180:
         ta,tb = a+45,b-2
         itera3 = 0
         itera4 = 0
         itera5 = 0
         balao2(game_display,falas2[int(itera2/90)%len(falas2)],ta,tb)
        if itera3>1 and itera3<90:
         tx,ty = x+25,y-2
         itera4 = 0
         itera5 = 0 
         balao(game_display,falas3[int(itera3/90)%len(falas3)],tx,ty)
        if itera4>1 and itera4<180:
         ta,tb = a+45,b-2
         itera5 = 0
         balao2(game_display,falas4[int(itera4/90)%len(falas4)],ta, tb)
        if itera5>1 and itera5<90:
         tx,ty = x+25,y-2
         balao(game_display,falas5[int(itera5/90)%len(falas5)],tx,ty) 


        pygame.display.update()
        clock.tick(30)
        itera += 1
        itera2 += 1
        itera3 += 1
        itera4 += 1
        itera5 += 1




pygame.quit()
quit()
