import math, pygame, random

SCREEN = {
    "x": 800,
    "y": 600
    }


dim = (SCREEN["x"]//2), (SCREEN["y"] // 2)


SEA = (153,50,204)
LIGHT = (238,130,238)

pygame.init()
tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("TP3 - Python - Questão 16")
new_star = False

def drawStar(ins, out, side, hole):
    inside = ins
    outside = out
    side = side

    seq = [ins, out] * 5
    a = [-50 + a for a in range(0, 600,36)]

    ps = [pygame.math.Vector2() for k in range(0,10)]

    for x, rad, out in zip(ps, seq, a):
        x.from_polar((rad*side,out))   
    return tuple((p + pygame.math.Vector2(hole) + (pygame.math.Vector2(0,side))) for p in ps)

ops = True
while ops:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ops = False
        elif event.type == pygame.MOUSEBUTTONUP:
            dim = pygame.mouse.get_pos()
            tam = random.randint(20,300)
            cor = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
            new_star = True
    tela.fill(SEA)
    if new_star:
        pygame.draw.polygon(tela, cor,  drawStar(1, 0.3, tam, dim))
    pygame.display.update()

pygame.quit()
