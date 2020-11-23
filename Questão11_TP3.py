import pygame

pygame.init()

SCREEN = {
    "x": 400,
    "y": 600
    }


BLUE = (0,0,255)
BLACK = (0, 0, 0)

tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("Mariana Bührer Sukevicz - TP3 - Questão 11")


x1 = SCREEN["x"] // 2
y1 = SCREEN["y"] // 2

def drawCircle(): 
    radian = 50    
    pygame.draw.circle(tela, BLUE, (x1, y1), radian)

vel_clock = pygame.time.Clock()

moving = 4

pygame.display.flip() 
pygame.key.set_repeat(100, 100)

while True:
    tela.fill(BLACK)
    x1 += moving
    if x1 == SCREEN["x"]:
        x1 = 0
    
    drawCircle()
    pygame.display.flip()    
    vel_clock.tick(100)
 
pygame.quit()
