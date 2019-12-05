"""
Arquivo principal do jogo
"""
import pygame
from classe_personagem import Soldado
from classe_aviao import Airplane
from auxiliar import tela, larguraTela, alturaTela, display_message, clock

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
        perY=alturaTela * 0.85,
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

    while True:
        tela.fill((0, 0, 0))

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
                    if carlinhos.perY >= alturaTela - carlinhos.perH:
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

    while True:
        tela.fill((0, 0, 0))

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
                    tracao = -80000
                # direita
                elif event.key == pygame.K_RIGHT:
                    tracao = 80000
                # mudar de figura
                elif event.key == pygame.K_ESCAPE:
                    soldado_loop()
                # cima
                elif event.key == pygame.K_UP:
                    angulo += 10
                # baixo
                elif event.key == pygame.K_DOWN:
                    angulo += -10

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tracao = 0

        aviao.forca(angulo, tracao)

        if aviao.atualizaX():
            aviao.draw()

        if aviao.atualizaY():
            aviao.draw()

        if aviao.combustivel():
            game_start()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()
    pygame.quit()
    quit()