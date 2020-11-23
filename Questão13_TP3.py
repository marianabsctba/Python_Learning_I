iimport pygame


COMPRIMENTO = 500
ALTURA = 500

GREEN = (0,128,0)
YELLOW = (255, 255, 0)

pygame.init()
tela = pygame.display.set_mode((COMPRIMENTO, ALTURA))
pygame.display.set_caption("Questão 13")

posx = COMPRIMENTO // 2
posy = ALTURA // 2


def drawCircle():
    radian = 50
    pygame.draw.circle(tela, GREEN, (posx, posy), radian)

mov1 = 1
mov2 = 2

ops = True
while ops:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ops= False
    if mov2 > 80:
        ops = False
    
    elif posx < 50 or posx > ALTURA - 50:
        mov1 *= -1
        mov2 += 1
    
    posx += mov1 * mov2
    tela.fill((YELLOW))
    pygame.time.delay(5)
    drawCircle()
    pygame.display.update()

pygame.display.quit()
pygame.quit()
