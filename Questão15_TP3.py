import math, pygame

SCREEN = {
    "x": 800,
    "y": 600
    }


dim = (SCREEN["x"]//2), (SCREEN["y"] // 2)


SEA = (153,50,204)
LIGHT = (238,130,238)

pygame.init()
tela = pygame.display.set_mode((SCREEN["x"], SCREEN["y"]))
pygame.display.set_caption("TP3 - Python - Questão 15")


def drawStar(ins, out, side, hole):
    inside = ins = 3
    outside = out = 1
    side = side

    seq = [ins, out] * 10
    a = [-50 + a for a in range(0, 600,36)]

    ps = [pygame.math.Vector2() for k in range(0,10)]

    for v, rad, out in zip(ps, seq, a):
        v.from_polar((rad*side,out))
   
    return tuple((p + pygame.math.Vector2(hole)) for p in ps)

ops = True
while ops:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ops = False

    tela.fill(SEA)
    pygame.draw.polygon(tela, LIGHT,  drawStar(1, 0.3, 100, dim))
    pygame.display.update()

pygame.quit()
