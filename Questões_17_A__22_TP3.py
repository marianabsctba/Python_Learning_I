import pygame, sys, os
from pygame.locals import *


LARGURA_TELA = 750
ALTURA_TELA = 500

LARGURA_LINHA = 10
PALETA_TAMANHO = 50
PALETAOFFSET = 20

PRETO = (0,0,0)
BRANCO = (255,255,255)

FPS = 200

def desenhaArena():
    DISPLAYSURF.fill(PRETO)
    pygame.draw.rect(DISPLAYSURF, BRANCO, ((0,0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA*2)
    pygame.draw.line(DISPLAYSURF, BRANCO, ((LARGURA_TELA//2), 0),((LARGURA_TELA//2), ALTURA_TELA), (LARGURA_LINHA//4))
def desenhaPaleta(paleta):
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    
    pygame.draw.rect(DISPLAYSURF, BRANCO, paleta)
    
def desenhaBola(bola):
    pygame.draw.rect(DISPLAYSURF, BRANCO, bola)
    
def moveBola(bola, bolaDirX, bolaDirY, velocidade):
    bola.x += bolaDirX * velocidade
    bola.y += bolaDirY * velocidade
    return bola

def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top <= (LARGURA_LINHA) or bola.bottom >= (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left <= (LARGURA_LINHA) or bola.right >= (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY

def inteligenciaArtificial(bola, bolaDirX, paleta2):
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2

def verificaPlacar10(placar, ten_points):
    if placar%10 == 0 and placar != 0:
        ten_points.play()
        return False
    return True

def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX, paleta_s):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        paleta_s.play()
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        paleta_s.play()
        return -1
    else:
        return 1

def contaColisao(bola, paleta1, bolaDirX, contador_velocidade):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom and contador_velocidade < 10:
        contador_velocidade += 1
        return contador_velocidade
    else:
        return contador_velocidade
    
def verificaPlacar(paleta1, bola, placar, bolaDirx, pontuacao, victory_s, defeat_s, ten_points):
    if bola.left <= LARGURA_LINHA:
        defeat_s.play()
        return 0
    elif bola.right >= LARGURA_TELA - LARGURA_LINHA:
        placar += 10
        if verificaPlacar10(placar, ten_points):
            victory_s.play()
        return placar
    elif bolaDirx == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += pontuacao
        verificaPlacar10(placar, ten_points)
        return placar
    else:
        return placar
    
def aumentaVelocidade(velocidade, contador_velocidade):
    if contador_velocidade == 10:
        velocidade += 1
        contador_velocidade = 0
    return velocidade, contador_velocidade

def aumentaPontuacao(velocidade, pontuacao, contador_velocidade, contador_pontuacao):
    if contador_velocidade == 10:
        contador_pontuacao += 1
    if contador_pontuacao == 2:
        pontuacao += 1
        contador_pontuacao = 0
    return pontuacao, contador_pontuacao

def desenhaPlacar(placar, velocidade):
    resultadoSurf = BASICFONT.render(f'vel = {velocidade}       placar = {placar}', True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 250, 25)
    DISPLAYSURF.blit(resultadoSurf, resultadoRect)

def main():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_visible(0)
    global DISPLAYSURF
    
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("PongNet")
    
    # Sons
    paleta_s = pygame.mixer.Sound('paleta.wav')
    paleta_s.set_volume(0.8)
    victory_s = pygame.mixer.Sound('victory.wav')
    victory_s.set_volume(0.5)
    defeat_s = pygame.mixer.Sound('defeat.wav')
    defeat_s.set_volume(0.5)
    ten_points = pygame.mixer.Sound('ten_points.wav')
    defeat_s.set_volume(0.8)
    
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    placar = 0
    contador_velocidade = 0
    velocidade = 2
    pontuacao = 1
    contador_pontuacao = 0
    
    bolaDirX = -1
    bolaDirY = -1
    
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)
    
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)

    while True:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                paleta1.y = mouseY
                
        desenhaArena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)
        
        bola = moveBola(bola, bolaDirX, bolaDirY, velocidade)
        contador_velocidade = contaColisao(bola, paleta1, bolaDirX, contador_velocidade)
        bolaDirX, bolaDirY = verificaColisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX, paleta_s)
        paleta2 = inteligenciaArtificial(bola, bolaDirX, paleta2)

        pontuacao, contador_pontuacao = aumentaPontuacao(velocidade, pontuacao, contador_velocidade, contador_pontuacao)
        velocidade, contador_velocidade = aumentaVelocidade(velocidade, contador_velocidade)
                
        placar = verificaPlacar(paleta1, bola, placar, bolaDirX, pontuacao, victory_s, defeat_s, ten_points)
        desenhaPlacar(placar, velocidade)

        pygame.display.update() 
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()

