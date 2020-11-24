#As questões 17 a 22 constam em um só arquivo e estão indicadas nos comentários.
# Foi utilizado o arquivo original, mas com as modificações solicitadas.

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

def arena():
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
    
    
def moveBola(bola, bolaDirX, bolaDirY, velocidade):# início da implementação do código solicitado na Questão 17 (aumento da velocidade pela colisão)
    bola.x += bolaDirX * velocidade
    bola.y += bolaDirY * velocidade
    return bola


def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top <= (LARGURA_LINHA) or bola.bottom >= (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left <= (LARGURA_LINHA) or bola.right >= (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY


def monitoraVelocidade(bola, paleta1, bolaDirX, cv): # início da implementação do código solicitado na Questão 17 (aumento da velocidade pela colisão)
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom and cv < 10:
        cv += 1
        return cv
    else:
        return cv


def verificaColisaoB(bola, paleta1, paleta2, bolaDirX, sound_paleta): # inserção do requisito da Questão 19 de som por colisão da bola 
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        sound_paleta.play()
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        sound_paleta.play()
        return -1
    else:
        return 1

def inteligenciaArtificial(bola, bolaDirX, paleta2):
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2

    
def verificaPlacar(paleta1, bola, placar, bolaDirx, pontuacao, winner, ohno, pontos): #sons das Questões 19 a 22 (verif. do placar + paletas + sons)
    if bola.left <= LARGURA_LINHA:
        ohno.play()
        return 0
    elif bola.right >= LARGURA_TELA - LARGURA_LINHA:
        placar += 10
        if verifica_dez(placar, pontos):
            winner.play()
        return placar
    elif bolaDirx == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += pontuacao
        verifica_dez(placar, pontos)
        return placar
    else:
        return placar


def verifica_dez(placar, ten_points): #inclusão de código (Questão 22) que toca música aos 10 pontos.
    if placar%10 == 0 and placar != 0:
        ten_points.play()
        return False
    return True
    

def pontua(velocidade, pontuacao, cv, cp):# considerando o aumento de velocidade implementado
    if cv == 10:
        cp += 1
    if cp == 2:
        pontuacao += 1
        cp = 0
    return pontuacao, cp

def desenhaPlacar(placar): #influência da velocidade da bola no placar (Questão 18)
    resultadoSurf = BASICFONT.render(f'placar = {placar}', True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 250, 25)
    DISPLAYSURF.blit(resultadoSurf, resultadoRect)
    

def aumentaVelocidade(velocidade, cv):
    if cv == 10:
        velocidade += 1
        cv = 0
    return velocidade, cv


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
    

      
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2
    
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    
    
    cv = 0
    velocidade = 2
    
    placar = 0
    pontuacao = 1
    cp = 0
    
    sound_paleta = pygame.mixer.Sound('paleta.ogg')
    sound_paleta.set_volume(1)
    winner = pygame.mixer.Sound('winner.mp3')
    winner.set_volume(1)
    ohno = pygame.mixer.Sound('ohno.wav')
    ohno.set_volume(1)
    pontos = pygame.mixer.Sound('pontos.mp3')
    pontos.set_volume(1)
    
    bolaDirX = -1
    bolaDirY = -1
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)
    
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA, PALETA_TAMANHO)    
       
    arena()
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
                
        arena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)
        
        bola = moveBola(bola, bolaDirX, bolaDirY, velocidade)
        paleta2 = inteligenciaArtificial(bola, bolaDirX, paleta2)
        
        placar = verificaPlacar(paleta1, bola, placar, bolaDirX, pontuacao, winner, ohno, pontos)
        pontuacao, cp = pontua(velocidade, pontuacao, cv, cp)
        
        cv = monitoraVelocidade(bola, paleta1, bolaDirX, cv)
        velocidade, cv = aumentaVelocidade(velocidade, cv)
        
        bolaDirX, bolaDirY = verificaColisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoB(bola, paleta1, paleta2, bolaDirX, sound_paleta)   
          
        desenhaPlacar(placar)

        pygame.display.update() 
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
