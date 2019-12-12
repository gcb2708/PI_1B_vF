"""
Arquivo para criação da classe Serra
"""
import pygame
from auxiliar import tela


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
        self.hitbox = (self.x, self.y, self.larg - 10, self.alt)
        if self.aniCount >= 8:
            self.aniCount = 0
        tela.blit(pygame.transform.scale(self.img[self.aniCount // 2], (50, 50)), (self.x, self.y))
        self.aniCount += 1
        pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)

    def colisao(self, rect):
        if rect[0] + rect[2] >= self.hitbox[0] or rect[0] <= self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

