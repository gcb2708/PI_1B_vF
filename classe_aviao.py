"""
Arquivo para criação da classe Aviao
"""
from auxiliar import tela, larguraTela, alturaTela, fuel_message, display_message
import time
import math
import pygame


class Airplane(object):

    def __init__(self, airX, airY, airW, airH, airImg):
        self.airX = airX                        # Posição do avião no eixo X
        self.airY = airY                        # Posição do avião no eixo Y
        self.airW = airW                        # Largura da imagem do avião
        self.airH = airH                        # Altura da imagem do avião
        self.airImg = airImg                    # Imagem do avião
        self.airVelX = 0                        # Velocidade HORIZONTAL
        self.airVelY = 0                        # Velocidade VERTICAL
        self.airAX = 0                          # Aceleração HORIZONTAL
        self.airAY = 0                          # Aceleração VERTICAL
        self.gravity = 9.86                     # Aceleração gravitacional do avião
        self.massa = 30000                      # Massa do avião
        self.peso = self.massa * self.gravity   # Força peso
        self.fuel = 100                         # Combustível
        self.count_f = 0                        # Contador para o combustível
        self.airVelTotal = 0                    # Velocidade total do avião
        self.Frx = 0                            # Força resultante em X
        self.Fry = 0                            # Força resultante em Y
        self.d = 1.2                            # Densidade do ar quando a temperatura é de 5ºC
        self.A = 1000                           # Área das asas avião
        self.Cd = 0.031                         # Coeficiente de arrasto
        self.D = 0                              # Força de arrasto
        self.Cs = 0.031                         # Coeficiente de arrasto
        self.S = 0                              # Força de sustentação
        self.teste_decolagem = False            # Teste se o avião já decolou
        self.teste_combustivel = False          # Para evitar bugs no contador de combustível

    def draw(self, angulo):
        tela.blit(pygame.transform.rotate(self.airImg, angulo), (self.airX, self.airY))

    def forca(self, angulo, tracao):
        # Cálculo do ângulo em radianos
        angulo = angulo * math.pi / 180
        # Cálculo do modulo da velocidade resultante
        self.airVelTotal = (self.airVelX ** 2 + self.airVelY ** 2) ** (1 / 2)

        # Cálculo da força de arrasto
        self.D = (1 / 2) * self.Cd * self.d * self.A * (self.airVelTotal ** 2)
        # Cálculo da força de sustentação
        self.S = (1 / 2) * self.Cs * self.d * self.A * (self.airVelTotal ** 2)

        # Se a velocidade VERTICAL é zero
        if self.airVelY == 0:
            self.Frx = tracao * math.cos(angulo) - self.D
            self.Fry = self.peso - self.S - tracao * math.sin(angulo)

        # Se a velocidade VERTICAL é diferente de zero
        elif self.airVelY != 0:
            self.Frx = tracao * math.cos(angulo) - self.D * (self.airVelX / self.airVelTotal) - self.S * \
                       (self.airVelY / self.airVelTotal)
            self.Fry = self.peso - tracao * math.sin(angulo) + self.D * (self.airVelY / self.airVelTotal) - \
                       self.S * (self.airVelX / self.airVelTotal)

        # Cálculo da aceleração no eixo X
        self.airAX = self.Frx / self.massa
        # Cálculo da aceleração no eixo X
        self.airAY = self.Fry / self.massa

    # Atualiza a posição HORIZONTAL do avião
    def atualizaX(self):
        # atualiza velocidade horizontal
        self.airVelX += self.airAX * (1 / 60)

        # verificar se a velociade é máxima
        if self.airVelX >= 500:
            self.airVelX = 500
        elif self.airVelX <= -500:
            self.airVelX = -500

        # atualiza posição horizontal
        self.airX += self.airVelX * (1 / 60) + 0.5 * self.airAX * ((1 / 60) ** 2)

        # limita direita
        if self.airX > 400:
            self.airX = 400
            # self.airVelX = 0
        # limita esquerda
        elif self.airX <= 0:
            self.airX = 0
            # self.airVelX = 0
        return True

    # Atualiza a posição VERTICAL do avião
    def atualizaY(self):
        # atualiza velocidade vertical
        self.airVelY += self.airAY * (1 / 60)

        # verificar se a velociade é máxima
        if self.airVelY >= 500:
            self.airVelY = 500
        elif self.airVelY <= -500:
            self.airVelY = -500

        # atualiza posição vertical
        self.airY += self.airVelY * (1 / 60) + 0.5 * (self.airAY) * ((1/60) ** 2)

        # limita inferiormente
        if self.airY > 390:
            self.airY = 390
            self.airVelY = 0

        # limita superiormente
        elif self.airY < 20:
            self.airY = 20
            self.airVelY = 0

        # Se o avião saiu da posição inicial
        if self.airVelY < 0 and self.airVelX != 0:
            self.teste_combustivel = True
            # Verificar se o avião decolou
            if self.airY < 350:
                self.teste_decolagem = True

        return True

    # Atualiza o combustível do avião
    def combustivel(self):
        # Primeiramente, verifica se o avião levantou voo
        if self.teste_combustivel:
            # Atualizar o valor do combustível
            if self.count_f >= 100:
                self.count_f = 0
            else:
                self.count_f += 0.001
                self.fuel -= 0.01

            # Verifica se tem aceleração em alguma direção
            if self.airAX != 0 or self.airAY != 0:
                self.fuel -= 0.02

        # Verifica se o combustível acabou
        if self.fuel <= 0:
            self.airAY = 0
            self.airAX = 0
            self.fuel = 0
            display_message("Sem combustível!!!!", (255, 255, 255))

            # Se chegou na base da tela sem combustível
            if self.airY >= 389:
                return True

        # Mostra o combustível
        fuel_message("Combustível: {:.2f} %".format(self.fuel), (255, 255, 255))

    # Colisão do avião
    def collide(self):
        # Chegou ao final da tela depois de decolar
        if self.airY > 389 and self.teste_decolagem is True:
            return True