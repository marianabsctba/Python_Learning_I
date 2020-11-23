import pygame

SCREEN = {
    "x": 600,
    "y": 800
    }

BLACK = (0,0,0)
VIOLET = (139,0,139)

pos_x = (SCREEN["x"] // 2) - 25
pos_y= (SCREEN["y"] // 2) - 25

pygame.init()
tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("Mariana Bührer Sukevicz - TP3 - Questão 14")

def drawSquare(): 
    pygame.draw.rect(tela, VIOLET, (pos_x, pos_y, 50, 50))
    
ops = True
while ops:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ops = False
        if evento.type == pygame.MOUSEBUTTONUP:
             pos_x = pygame.mouse.get_pos()[0]
             pos_y = pygame.mouse.get_pos()[1] 

    tela.fill(BLACK)
    drawSquare()
    pygame.display.update()

pygame.display.quit()
pygame.quit()
