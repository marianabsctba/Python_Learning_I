import pygame

SCREEN = {
    "x": 800,
    "y": 600
    }


BLUE = (0,0,255)

pygame.init()
tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("Mariana Bührer Sukevicz - TP3 - Fund. Python")

 
def drawCircle(SCREEN): 
    radian = 50    
    xpos = SCREEN["x"] // 2
    ypos = SCREEN["y"] // 2
    circ = pygame.draw.circle(tela, BLUE, (xpos, ypos), radian)
    

terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            
        drawCircle(SCREEN)
        pygame.display.update()
                 
pygame.display.quit()
