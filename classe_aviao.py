"""
Arquivo para criação da classe Aviao
"""
from auxiliar import tela, larguraTela, alturaTela, fuel_message, display_message
import time
import math


class Airplane(object):

    def __init__(self, airX, airY, airW, airH, airImg):
        self.airX = airX  # Posição do avião no eixo X
        self.airY = airY  # Posição do avião no eixo Y
        self.airW = airW  # Largura da imagem do avião
        self.airH = airH  # Altura da imagem do avião
        self.airImg = airImg  # Imagem do avião
        self.airVelX = 0  # Velocidade HORIZONTAL
        self.airVelY = 0  # Velocidade VERTICAL
        self.airAX = 0  # Aceleração HORIZONTAL
        self.airAY = 0  # Aceleração VERTICAL

        self.gravity = 52.3  # Aceleração gravitacional do avião
        self.fuel = 100  # Combustível
        self.count_f = 0  # Contador para o combustível
        self.airVelTotal = 0  # Velocidade total do avião
        self.Frx = 0  # Força resultante em X
        self.Fry = 0  # Força resultante em Y
        self.densidade_meio = 0.208  # Densidade do ar quando a temperatura é de 5ºC
        self.area_objeto = 170  # Área das asas avião
        self.coef_arrasto = 0.031  # Coeficiente de arrasto
        self.forca_arrasto = 0  # Força de arrasto
        self.massa = 100  # Massa do avião
        self.peso = self.massa * self.gravity  # Força peso
        self.coef_sustentacao = 0.031  # Coeficiente de arrasto
        self.forca_sustentacao = 0  # Força de sustentação

    def draw(self):
        tela.blit(self.airImg, (self.airX, self.airY))

    def forca(self, angulo, tracao):
        # Cálculo do ângulo em radianos
        angulo = angulo * math.pi / 180
        # Cálculo da força resultante no eixo X
        self.Frx = tracao * math.cos(angulo) - self.forca_arrasto * math.cos(
            angulo) - self.forca_sustentacao * math.sin(angulo)
        # Cálculo da aceleração no eixo X
        self.airAX = self.Frx / self.massa

        # Cálculo da força resultante no eixo Y
        self.Fry = self.forca_arrasto * math.sin(angulo) + self.peso - tracao * math.sin(
            angulo) - self.forca_sustentacao * math.cos(angulo)
        # Cálculo da aceleração no eixo X
        self.airAY = self.Fry / self.massa
        # Cálculo do modulo da velocidade resultante
        self.airVelTotal = (self.airVelX ** 2 + self.airVelY ** 2) ** (1 / 2)

        # Cálculo da força de arrasto
        self.forca_arrasto = (1 / 2) * self.coef_arrasto * self.densidade_meio * self.area_objeto * (
                    self.airVelTotal ** 2)
        # Cálculo da força de sustentação
        self.forca_sustentacao = (1 / 2) * self.coef_sustentacao * self.densidade_meio * self.area_objeto * (
                    self.airVelTotal ** 2)

        if self.airVelX < 0:
            self.forca_arrasto = 0
            self.forca_sustentacao = 0

        print(angulo)

    # Atualiza a posição HORIZONTAL do avião
    def atualizaX(self):
        # atualiza velocidade horizontal
        self.airVelX += self.airAX * (1 / 60)

        # verificar se a velociade é máxima
        if self.airVelX >= 200:
            self.airVelX = 200
        elif self.airVelX <= -200:
            self.airVelX = -200

        # atualiza posição horizontal
        self.airX += self.airVelX * (1 / 60) + 0.5 * self.airAX * ((1 / 60) ** 2)

        # limita direita
        if self.airX > larguraTela - self.airW:
            self.airX = larguraTela - self.airW
            self.airVelX = 0
        # limita esquerda
        elif self.airX < 0:
            self.airX = 0
            self.airVelX = 0
        return True

    # Atualiza a posição VERTICAL do avião
    def atualizaY(self):
        # atualiza velocidade vertical
        self.airVelY += (self.airAY) * (1 / 60)

        # verificar se a velociade é máxima
        if self.airVelY >= 200:
            self.airVelY = 200
        elif self.airVelY <= -200:
            self.airVelY = -200

        # atualiza posição vertical
        self.airY += self.airVelY * (1 / 60) + 0.5 * (self.airAY) * ((1 / 60) ** 2)

        # limita inferiormente
        if self.airY > alturaTela - self.airH:
            self.airY = alturaTela - self.airH
            self.airVelY = 0
        # limita superiormente
        elif self.airY < 0:
            self.airY = 0
            self.airVelY = 0
        return True

    def combustivel(self):
        # altualizar o valor do combustível
        if self.count_f >= 100:
            self.count_f = 0
        else:
            self.count_f += 0.001
            self.fuel -= 0.0001

        # verifica se o combustível acabou
        if self.fuel <= 0:
            self.airAY = 0
            self.airAX = 0
            self.fuel = 0
            display_message("Sem combustível!!!!", (255, 255, 255))

            # se chegou na base da tela sem combustível
            if self.airY >= alturaTela - self.airH:
                time.sleep(2)
                return True

        # verifica se o avião levantou voo
        if self.airX <= 0 and self.airY >= alturaTela - self.airH:
            self.fuel = 100

        # verifica se tem aceleração em alguma direção
        if self.airAX != 0 or self.airAY != 0:
            self.fuel -= 0.0002

        # Mostra o combustível
        fuel_message("Combustível: {:.2f} %".format(self.fuel), (255, 255, 255))