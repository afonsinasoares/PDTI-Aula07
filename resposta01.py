# 1. Classe Bola: Crie uma classe que modele uma bola:
# A. Atributos: Cor, circunferência, material
# B. Métodos: trocaCor e mostraCor
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def troca_cor(self, cor):
        self.__cor = cor

    def mostra_cor(self):
        return self.__cor

# Testa classe
bola_futebol = Bola('branco', 3.5, 'couro')

print(bola_futebol.mostra_cor())

bola_futebol.troca_cor('azul')

print(bola_futebol.mostra_cor())

bola_futebol._Bola__cor = 'Preto'

print(bola_futebol._Bola__cor)