# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# A. Atributos: Tamanho do lado
# B. Métodos: Mudar valor do Lado,
#    Retornar valor do Lado e calcular Área
class Quadrado:
    def __init__(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def muda_tamanho_lado(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def exibe_tamanho_lado(self):
        return self.__tamanho_lado

    def calcula_area(self):
        return self.__tamanho_lado * self.__tamanho_lado

q1 = Quadrado(4)
print(q1.calcula_area())

q1.muda_tamanho_lado(5)
print(q1.calcula_area())