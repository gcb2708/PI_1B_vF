"""
Arquivo para criação do fluido
"""


class Fluido(object):

    def __init__(self):
        self.densidade_meio = 0
        self.area_objeto = 0
        self.coef_arrasto = 0
        self.forca_arrasto = 0

    def arrasto(self, velocidade):
        pass
