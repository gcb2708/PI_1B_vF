"""
Arquivo principal do jogo
"""
# import pygame
import random
from classe_personagem import Soldado
from classe_aviao import Airplane
from classe_serra import Serra
from auxiliar import *
from pygame.locals import *

pygame.init()

loop_teste = 0


def game_start():
    # carregar as imagens do menu
    Fase1 = pygame.transform.scale(pygame.image.load('Img/Menu/Fase1.png'), (150, 100))
    Fase2 = pygame.transform.scale(pygame.image.load('Img/Menu/Fase2.png'), (150, 100))
    Sair = pygame.transform.scale(pygame.image.load('Img/Menu/Sair.png'), (150, 100))

    # carlao = pygame.transform.scale(pygame.image.load('Img/Crash/Crash.png'), (800, 600))

    intro = True
    teste_fase1 = False
    teste_fase2 = False
    teste_sair = False

    # posição das imagens do menu
    posF1 = (330, 200)
    posF2 = (330, 320)
    posS = (330, 440)
    while intro:
        tela.fill((255, 255, 255))
        # tela.blit(carlao, (0, 0))
        tela.blit(Fase1, posF1)
        tela.blit(Fase2, posF2)
        tela.blit(Sair, posS)
        menu_message('Soldado Carlinhos', (0, 0, 255))

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # mudança de posição do mouse
            if event.type == pygame.MOUSEMOTION:
                # se estiver dentro do intervado que contém as imagens, o teste é verdadeiro
                if posF1[0] <= event.pos[0] <= posF1[0] + 140:
                    if posF1[1] <= event.pos[1] <= posF1[1] + 100:
                        teste_fase1 = True
                # caso contrário
                else:
                    teste_fase1 = False
                # se estiver dentro do intervado que contém as imagens, o teste é verdadeiro
                if posF2[0] <= event.pos[0] <= posF2[0] + 140:
                    if posF2[1] <= event.pos[1] <= posF2[1] + 100:
                        teste_fase2 = True
                # caso contrário
                else:
                    teste_fase2 = False
                # se estiver dentro do intervado que contém as imagens, o teste é verdadeiro
                if posS[0] <= event.pos[0] <= posS[0] + 140:
                    if posS[1] <= event.pos[1] <= posS[1] + 100:
                        teste_sair = True
                # caso contrário
                else:
                    teste_sair = False

            # botão do mouse foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                # caso queira jogar novamente
                if teste_fase1:
                    if event.button == 1:
                        soldado_loop()
                # caso queira voltar para o menu
                elif teste_fase2:
                    if event.button == 1:
                        mct_loop()
                # caso queira sair
                elif teste_sair:
                    if event.button == 1:
                        intro = False
                        quit()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def soldado_loop():
    global loop_teste
    # Criando o personagem com o modelo da classe Soldado
    carlinhos = Soldado(
        perX=larguraTela * 0.45,
        perY=alturaTela * 0.7,
        perW=88,
        perH=88,
        perImg=pygame.image.load('Img/SoldadoRight/R00.png')
    )

    # verificar o lado do movimento
    esquerda = False
    direita = False
    # variável de teste para verificar o lado que o personagem para
    teste_dir = 1
    # testa para o pulo
    teste_pulo = False
    # boost
    boost = 0
    # side-scroller
    fundoTela = pygame.image.load('Img/Backgrounds/bg_per_2_dim.png').convert()
    xTela1 = 0
    xTela2 = fundoTela.get_width()
    pygame.time.set_timer(USEREVENT+1, random.randrange(2000, 3500))
    obstacles = []
    loop = True

    while loop:
        tela.blit(fundoTela, (xTela1, 0))
        tela.blit(fundoTela, (xTela2, 0))

        for serra in obstacles:
            serra.draw()
            if serra.collide(carlinhos.hitbox):
                menu_message("Você Perdeu!", (0, 0, 0))
                pygame.time.delay(1000)
                loop = False
                loop_teste = 1
                endScreen()
            if carlinhos.perX == 450 and direita is True:
                if boost == 0:
                    serra.x -= 3
                else:
                    serra.x -= 4
            if serra.x < serra.larg * -1:
                obstacles.pop(obstacles.index(serra))

        # Se o personagem estiver dentro da região delimitada
        # ou estiver parado, a tela não anda
        if 0 <= carlinhos.perX < 450:
            xTela1 -= 0
            xTela2 -= 0
        # Mas se estiver exatamente no limiar da região e
        # estiver se movendo, a tela anda também
        if carlinhos.perX == 450 and direita is True:
            # Se NÃO tem boost, a tela anda mais devagar
            if boost == 0:
                xTela1 -= 3
                xTela2 -= 3
            # Se tem boost, anda mais rápido
            else:
                xTela1 -= 4
                xTela2 -= 4

        # "Joga o fundo de volta no fim da tela para aproveitar a imagem"
        if xTela1 < fundoTela.get_width() * (-1):
            xTela1 = fundoTela.get_width()
        if xTela2 < fundoTela.get_width() * (-1):
            xTela2 = fundoTela.get_width()

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # botao foi pressionado
            if event.type == pygame.KEYDOWN:

                # esquerda
                if event.key == pygame.K_LEFT:
                    carlinhos.perVelX = -252.72
                    esquerda = True
                    direita = False
                    teste_dir = 0

                # direita
                elif event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 252.72
                    esquerda = False
                    direita = True
                    teste_dir = 1

                # mudar de jogabilidade
                elif event.key == pygame.K_ESCAPE:
                    game_start()

                # verifica se está pulando
                elif event.key == pygame.K_SPACE:
                    if carlinhos.perY >= 408:
                        carlinhos.perVelY = -300
                        teste_pulo = True

                if event.key == pygame.K_LSHIFT:
                    if esquerda:
                        boost = -100
                    elif direita:
                        boost = 100

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 0
                    esquerda = False
                    direita = False
                    boost = 0

                if event.key == pygame.K_LSHIFT:
                    boost = 0

            if event.type == USEREVENT+1:
                r = 0  # random.randrange(0, 2)
                if r == 0:
                    obstacles.append(Serra(810, 438, 50, 50))

        carlinhos.pulo()

        if carlinhos.anda(boost):
            carlinhos.troca_frames(esquerda, direita, teste_dir, teste_pulo)

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def endScreen():
    global loop_teste
    # fase 1
    if loop_teste == 1:
        # imagens do fundo
        fundoTela = pygame.image.load('Img/Backgrounds/bg_per_2_dim.png').convert()
        cor = (0, 0, 0)

    # fase 2
    elif loop_teste == 2:
        # imagens do fundo
        fundoTela = pygame.image.load('Img/Backgrounds/bg_air_esp_2.jpg').convert()
        cor = (255, 255, 255)

    # fundo da tela
    tela.blit(fundoTela, (0, 0))
    # teste para jogar novamente
    simm = False
    naoo = False
    # imagens do menu
    menu_message('Quer jogar novamente?', cor)
    sim = pygame.transform.scale(pygame.image.load('Img/Menu/Sim.png'), (80, 60))
    nao = pygame.transform.scale(pygame.image.load('Img/Menu/Nao.png'), (80, 60))
    # posição das imagens
    pos1 = (120, 400)
    pos2 = (580, 400)

    while True:
        tela.blit(sim, (120, 400))
        tela.blit(nao, (580, 400))

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # botao foi pressionado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if loop_teste == 1:
                        soldado_loop()
                    elif loop_teste == 2:
                        mct_loop()
                if event.key == pygame.K_n:
                    game_start()

            # mudança de posição do mouse
            if event.type == pygame.MOUSEMOTION:
                # se estiver dentro do intervado que contém as imagens, o teste é verdadeiro
                if pos1[0] <= event.pos[0] <= pos1[0] + 100:
                    if pos1[1] <= event.pos[1] <= pos1[1] + 60:
                        simm = True
                # caso contrário
                else:
                    simm = False
                # se estiver dentro do intervado que contém as imagens, o teste é verdadeiro
                if pos2[0] <= event.pos[0] <= pos2[0] + 100:
                    if pos2[1] <= event.pos[1] <= pos2[1] + 60:
                        naoo = True
                # caso contrário
                else:
                    naoo = False
            # botão do mouse foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                # caso queira jogar novamente
                if simm:
                    if event.button == 1:
                        # Fase 1
                        if loop_teste == 1:
                            soldado_loop()
                        # Fase 2
                        elif loop_teste == 2:
                            mct_loop()
                # caso queira sair
                elif naoo:
                    if event.button == 1:
                        # Menu
                        game_start()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def mct_loop():
    global loop_teste

    # Criando o avião com o modelo da classe Airplane
    aviao = Airplane(airX=0,
                     airY=alturaTela - 128,
                     airW=128,
                     airH=128,
                     airImg=pygame.image.load('Img/aviao/MCT.png'))
    # tração dos motores do avião
    tracao = 0
    # ângulo de ataque do avião
    angulo = 0
    teste_angulo = False
    sentido_angulo = 0

    fundoTela = pygame.image.load('Img/Backgrounds/bg_air_esp_2.jpg').convert()
    xTela1 = 0
    xTela2 = fundoTela.get_width()

    while True:
        tela.blit(fundoTela, (xTela1, 0))
        tela.blit(fundoTela, (xTela2, 0))

        # Se o personagem estiver dentro da região delimitada
        # ou estiver parado, a tela não anda
        if 0 <= aviao.airX < 400:
            xTela1 -= 0
            xTela2 -= 0
        # Mas se estiver exatamente no limiar da região e
        # estiver se movendo, a tela anda também
        if aviao.airX == 400 and aviao.airVelX != 0:
            xTela1 -= 1.6
            xTela2 -= 1.6

        # "Joga o fundo de volta no fim da tela para aproveitar a imagem"
        if xTela1 < fundoTela.get_width() * (-1):
            xTela1 = fundoTela.get_width()
        if xTela2 < fundoTela.get_width() * (-1):
            xTela2 = fundoTela.get_width()

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # botao foi pressionado
            if event.type == pygame.KEYDOWN:
                # esquerda
                if event.key == pygame.K_LEFT:
                    tracao = -1000000
                # direita
                elif event.key == pygame.K_RIGHT:
                    tracao = 1000000
                    aviao.teste_combustivel = True
                # mudar de figura
                elif event.key == pygame.K_ESCAPE:
                    game_start()
                # cima
                elif event.key == pygame.K_UP:
                    teste_angulo = True
                    sentido_angulo = 1
                # baixo
                elif event.key == pygame.K_DOWN:
                    teste_angulo = True
                    sentido_angulo = -1

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tracao = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    teste_angulo = False
                    sentido_angulo = 0

        # Alterar o ângulo entre a tração e o eixo X,
        # se o botão foi pressionado
        if teste_angulo:
            # Sentido em que o ângo está mudando
            if sentido_angulo == 1:
                angulo += 0.2
            elif sentido_angulo == -1:
                angulo -= 0.2

            # Limita o angulo máximo do avião
            if angulo >= 30:
                angulo = 30
            elif angulo <= -30:
                angulo = -30

        aviao.forca(angulo, tracao)

        if aviao.atualizaX():
            aviao.draw(angulo)

        if aviao.atualizaY():
            aviao.draw(angulo)

        # Fim de jogo
        if aviao.combustivel() or aviao.collide():
            menu_message("Você Perdeu!", (255, 255, 255))
            pygame.time.delay(1000)
            loop_teste = 2
            endScreen()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()
    pygame.quit()
    quit()
