import pygame
from pygame.locals import *

pygame.init()

COMPRIMENTO = 640
ALTURA = 480

BLUE = (0,0,255)
YELLOW = (255, 255, 0)

tela = pygame.display.set_mode((COMPRIMENTO, ALTURA))
pygame.display.set_caption("Questão 12")

VEL_CLOCK = fpsClock = pygame.time.Clock()


x1 = COMPRIMENTO // 2
y1 = ALTURA // 2

radian = 50  

def drawCircle(): 
    pygame.draw.circle(tela, YELLOW, (x1, y1), radian)

mov1 = -1
mov2 = 1

pygame.display.flip()
pygame.key.set_repeat(100, 100)


ops = True
while ops:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ops = False
 
    act = pygame.key.get_pressed()    
 
    if act[K_LEFT]:
        x1 += mov1
        if x1 == -radian:
            x1 = 640
        
    elif act[K_RIGHT]:  
        x1 += mov2
        if x1 == COMPRIMENTO:
            x1= -50
    elif act[K_UP]:
        y1 += mov1
        if y1 == -radian:
            y1 = ALTURA
    elif act[K_DOWN]:
        y1 += mov2
        if y1 == ALTURA + radian:
            y1 = -radian
        
    tela.fill(BLUE)
    drawCircle()
    pygame.display.flip()
    VEL_CLOCK.tick(200)

pygame.display.quit()
pygame.quit()
exit()
