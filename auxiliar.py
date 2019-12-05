""""
Arquivo para definir questões auxiliares
"""
import pygame

larguraTela = 800
alturaTela = 600

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Soldado Carlinhos")
pygame.display.set_icon(pygame.image.load('Img/OutrasImagens/iconeTela.png'))
clock = pygame.time.Clock()

framesEsquerda = [pygame.image.load('Img/SoldadoLeft/L00.png'),
                  pygame.image.load('Img/SoldadoLeft/L01.png'),
                  pygame.image.load('Img/SoldadoLeft/L02.png'),
                  pygame.image.load('Img/SoldadoLeft/L03.png'),
                  pygame.image.load('Img/SoldadoLeft/L04.png'),
                  pygame.image.load('Img/SoldadoLeft/L05.png'),
                  pygame.image.load('Img/SoldadoLeft/L06.png'),
                  pygame.image.load('Img/SoldadoLeft/L07.png'),
                  pygame.image.load('Img/SoldadoLeft/L08.png'),
                  pygame.image.load('Img/SoldadoLeft/L09.png')]

framesDireita = [pygame.image.load('Img/SoldadoRight/R00.png'),
                 pygame.image.load('Img/SoldadoRight/R01.png'),
                 pygame.image.load('Img/SoldadoRight/R02.png'),
                 pygame.image.load('Img/SoldadoRight/R03.png'),
                 pygame.image.load('Img/SoldadoRight/R04.png'),
                 pygame.image.load('Img/SoldadoRight/R05.png'),
                 pygame.image.load('Img/SoldadoRight/R06.png'),
                 pygame.image.load('Img/SoldadoRight/R07.png'),
                 pygame.image.load('Img/SoldadoRight/R08.png'),
                 pygame.image.load('Img/SoldadoRight/R09.png')]

framesParado = [pygame.image.load('Img/SoldadoParado/SL1.png'),
                pygame.image.load('Img/SoldadoParado/SR1.png')]

framesPulo = [pygame.image.load('Img/SoldadoPulo/P00.png'),
              pygame.image.load('Img/SoldadoPulo/P01.png'),
              pygame.image.load('Img/SoldadoPulo/P02.png'),
              pygame.image.load('Img/SoldadoPulo/P03.png'),
              pygame.image.load('Img/SoldadoPulo/P04.png'),
              pygame.image.load('Img/SoldadoPulo/P05.png')]

framesPuloE = [pygame.image.load('Img/SoldadoPuloE/P00E.png'),
              pygame.image.load('Img/SoldadoPuloE/P01E.png'),
              pygame.image.load('Img/SoldadoPuloE/P02E.png'),
              pygame.image.load('Img/SoldadoPuloE/P03E.png'),
              pygame.image.load('Img/SoldadoPuloE/P04E.png'),
              pygame.image.load('Img/SoldadoPuloE/P05E.png')]

# renderiza o texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# apresenta texto na tela
def display_message(text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 70)

    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (larguraTela / 2, alturaTela / 2)

    tela.blit(TextSurf, TextRect)
    pygame.display.update()

def fuel_message(text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 15)

    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (90, 20)

    tela.blit(TextSurf, TextRect)
    pygame.display.update()