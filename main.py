"""
Arquivo principal do jogo
"""
import pygame
from classe_personagem import Soldado
from classe_aviao import Airplane
from auxiliar import *

pygame.init()


def game_start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    intro = False
                    soldado_loop()

        tela.fill((255, 255, 255))
        display_message("Press Enter", (255, 0, 255))
        clock.tick(15)


def soldado_loop():
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

    ################################
    fundoTela = pygame.image.load('Img/Backgrounds/bg_per_2_dim.png').convert()
    xTela1 = 0
    xTela2 = fundoTela.get_width()
    ################################

    while True:
        ###########################################
        tela.blit(fundoTela, (xTela1, 0))
        tela.blit(fundoTela, (xTela2, 0))

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
                xTela1 -= 1.6
                xTela2 -= 1.6
            # Se tem boost, anda mais rápido
            else:
                xTela1 -= 2.0
                xTela2 -= 2.0

        # "Joga o fundo de volta no fim da tela para aproveitar a imagem"
        if xTela1 < fundoTela.get_width() * (-1):
            xTela1 = fundoTela.get_width()
        if xTela2 < fundoTela.get_width() * (-1):
            xTela2 = fundoTela.get_width()
        ###########################################

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
                    mct_loop()

                # verifica se está pulando
                elif event.key == pygame.K_SPACE:
                    if carlinhos.perY >= 408:
                        carlinhos.perVelY = -300
                        teste_pulo = True
                        boost = 0

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

        carlinhos.pulo()

        if carlinhos.anda(boost):
            carlinhos.troca_frames(esquerda, direita, teste_dir, teste_pulo)

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def mct_loop():
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

    ################################
    fundoTela = pygame.image.load('Img/Backgrounds/bg_air_esp_2.jpg').convert()
    xTela1 = 0
    xTela2 = fundoTela.get_width()
    ################################

    while True:
        ###########################################
        tela.blit(fundoTela, (xTela1, 0))
        tela.blit(fundoTela, (xTela2, 0))

        # Se o personagem estiver dentro da região delimitada
        # ou estiver parado, a tela não anda
        if 0 <= aviao.airX < 400:
            xTela1 -= 0
            xTela2 -= 0
        # Mas se estiver exatamente no limiar da região e
        # estiver se movendo, a tela anda também
        if aviao.airX == 400:
            xTela1 -= 1.6
            xTela2 -= 1.6

        # "Joga o fundo de volta no fim da tela para aproveitar a imagem"
        if xTela1 < fundoTela.get_width() * (-1):
            xTela1 = fundoTela.get_width()
        if xTela2 < fundoTela.get_width() * (-1):
            xTela2 = fundoTela.get_width()
        ###########################################

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
                    tracao = -400000
                # direita
                elif event.key == pygame.K_RIGHT:
                    tracao = 400000
                # mudar de figura
                elif event.key == pygame.K_ESCAPE:
                    soldado_loop()
                # cima
                elif event.key == pygame.K_UP:
                    angulo += 1
                # baixo
                elif event.key == pygame.K_DOWN:
                    angulo += -1

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tracao = 0

        aviao.forca(angulo, tracao)

        if aviao.atualizaX():
            aviao.draw(angulo)

        if aviao.atualizaY():
            aviao.draw(angulo)

        if aviao.combustivel():
            game_start()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()
    pygame.quit()
    quit()
