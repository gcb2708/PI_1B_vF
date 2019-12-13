"""
Arquivo para criação da classe Serra
"""
import pygame
from auxiliar import *


class Serra(object):
    def __init__(self, x, y, larg, alt):
        self.x = x
        self.y = y
        self.larg = larg
        self.alt = alt
        self.hitbox = (x, y, larg, alt)
        self.aniCount = 0
        self.img = [pygame.image.load('Img/Serra/SAW0.png'),
                    pygame.image.load('Img/Serra/SAW1.png'),
                    pygame.image.load('Img/Serra/SAW2.png'),
                    pygame.image.load('Img/Serra/SAW3.png')]

    def draw(self):
        # Define a área da serra
        self.hitbox = (self.x, self.y, self.larg, self.alt)
        # Contador para a animação da serra
        if self.aniCount >= 8:
            self.aniCount = 0
        # Desenha a serra
        tela.blit(pygame.transform.scale(self.img[self.aniCount // 2], (50, 50)), (self.x, self.y))
        self.aniCount += 1
        # Desenha a área da serra
        pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        # Teste para colisão no eixo X
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            # Teste para colisão no eixo Y
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
