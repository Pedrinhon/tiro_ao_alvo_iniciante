import pygame
from random import randint

pygame.init()

largura = 640
altura = 480


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tiro ao Alvo")

clique = pygame.Sound("aprendendo_pygame/tiro_alvo/clique.wav")

fonte = pygame.font.SysFont(None, 36)

#Variaveis
ponto = 0
jogo = True

#Listas
alvos = []

#Função que desenha tudo
def desenhar():
    for alvo in alvos:
        pygame.draw.rect(tela,(255,0,0), alvo)
#Alvo
def alvo_criar():
    for i in range(2):
        x = randint(30,600)
        y = randint(30,440)
        alvo = pygame.Rect(x,y,40,60)
        alvos.append(alvo)
alvo_criar()

def pontuacao():
    global ponto, fonte
    texto = fonte.render(f"Pontos: {ponto}", True, (255,255,255))
    tela.blit(texto, (10,10))


while jogo:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        if event.type == pygame.MOUSEBUTTONUP:
            for alvo in alvos:
                pos = pygame.mouse.get_pos()
                if alvo.collidepoint(pos):
                    alvo.x = randint(30,600)
                    alvo.y = randint(30,440)
                    ponto = ponto + 1
                    clique.play()
    #Desenhar
    desenhar()
    pontuacao()

    pygame.display.update()

pygame.quit()
