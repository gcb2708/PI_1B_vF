"""
Arquivo para criação da classe Soldado
"""

from auxiliar import *

class Soldado(object):

    def __init__(self, perX, perY, perW, perH, perImg):
        self.perX = perX        # Posição do personagem no eixo X
        self.perY = perY        # Posição do personagem no eixo Y
        self.perW = perW        # Largura da imagem do personagem
        self.perH = perH        # Altura da imagem do personagem
        self.perImg = perImg    # Imagem do personagem
        self.perVelX = 0        # Velocidade HORIZONTAL do personagem
        self.perVelY = 0        # Velocidade Vertical do personagem
        self.perAY = 445.73     # Aceleração VERTICAL do personagem
        self.count = 0          # Contador dos frames do personagem
        self.count_p = 0        # Contador dos frames do pulo
        self.teste_boost = 0  # Teste para boost

    # Atualiza a posição HORIZONTAL do personagem
    def anda(self, boost):
        # varifica a posição do personagem no eixo Y
        if self.perY < alturaTela - self.perW:
            boost = 0

        self.perX += (self.perVelX + boost) * (1 / 60)

        # verificar se existe boost
        if boost != 0:
            self.teste_boost = -1
        else:
            self.teste_boost = 0

        if self.perX > larguraTela - self.perW:
            self.perX = larguraTela - self.perW

        elif self.perX < 0:
            self.perX = 0

        return True

    # Atualiza a posição VERTICAL do personagem
    def pulo(self):
        # Cálculo da velocidade VERTICAL do personagem
        self.perVelY += self.perAY * (1 / 60)
        # Cálculo da posição VERTICAL do personagem
        self.perY += self.perVelY * (1 / 60) + 0.5 * self.perAY * ((1 / 60) ** 2)
        # Limita a imagem inferiormente
        if self.perY > alturaTela - self.perH:
            self.perY = alturaTela - self.perH
            self.perVelY = 0
        return True

    # trocar os frames do personagem
    def troca_frames(self, esquerda, direita, teste_dir, teste_pulo):
        # contador andando
        if self.count + 1 >= 18:
            self.count = 0
        # contador pulando
        if self.count_p + 1 >= 36:
            self.count_p = 0

        # verifica a posição do personagem no eixo Y
        if self.perY >= alturaTela - self.perW:
            teste_pulo = False

        # o personagem está pulando
        if teste_pulo:

            if esquerda:
                tela.blit(framesPuloE[self.count_p // 6], (self.perX, self.perY))
                self.count_p += 1
            elif direita:
                tela.blit(framesPulo[self.count_p // 6], (self.perX, self.perY))
                self.count_p += 1

            # o personagem só tem movimento no eixo Y
            else:
                # teste da direção anterior
                if teste_dir == 0:
                    tela.blit(framesPuloE[self.count_p // 6], (self.perX, self.perY))
                    self.count_p += 1
                elif teste_dir == 1:
                    tela.blit(framesPulo[self.count_p // 6], (self.perX, self.perY))
                    self.count_p += 1

        # o personagem não está pulando
        elif not teste_pulo:
            if esquerda:
                # mudar frame dependo do boost
                tela.blit(framesEsquerda[self.count // (4 + self.teste_boost)], (self.perX, self.perY))
                self.count += 1

            elif direita:
                # mudar frame dependo do boost
                tela.blit(framesDireita[self.count // (4 + self.teste_boost)], (self.perX, self.perY))
                self.count += 1

            else:
                if teste_dir == 0 or teste_dir == 1:
                    tela.blit(framesParado[teste_dir], (self.perX, self.perY))
                    self.count = 0

        # personagem parado
        else:
            if teste_dir == 0 or teste_dir == 1:
                tela.blit(framesParado[teste_dir], (self.perX, self.perY))
                self.count = 0
        pygame.display.update()