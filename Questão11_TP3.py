import pygame

SCREEN = {
    "x": 800,
    "y": 600
    }

RUN = 200

RED = (255,0,0)
VIOLET = (238,130,238)

pygame.init()
tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("Mariana Bührer Sukevicz - TP3 - Questão 10")

x1 = SCREEN["x"] // 2
y2 = SCREEN["y"] // 2

def drawSquare(): 
    pygame.draw.rect(tela, RED, (x1, y2,100,100))
    
x1_run = 30
y2_run = -30


finish = True
while finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 -= x1_run
            elif event.key == pygame.K_DOWN:
                y2 += y2_run
            elif event.key == pygame.K_UP:
                x1 += x1_run
            elif event.key == pygame.K_RIGHT:
                y2 -= y2_run
        elif event.type == pygame.QUIT:
            finish= False
            
    tela.fill((VIOLET))
    drawSquare()
    pygame.display.update()

pygame.quit()
