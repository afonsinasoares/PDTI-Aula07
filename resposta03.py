# Classe Retangulo: Crie uma classe que modele um retangulo:
# A. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a
# escolher)
# B. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
# e calcular Perímetro;
# C. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
# informe as medidades de um local. Depois, deve criar um objeto com as
# medidas e calcular a quantidade de pisos e de rodapés necessárias para
# o local.

class Retangulo:

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def mudar_base(self, base):
        self.__base = base

    def mudar_altura(self, altura):
        self.__altura = altura

    def obter_base(self):
        return self.__base

    def obter_altura(self):
        return self.__altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        # pass (para não dar erro vc coloca pass
        # enquanto o método não tiver nenhuma linha de comando
        return 2 * self.__base + 2 * self.__altura

# Teste da classe Retangulo
paralelograma = Retangulo(5, 4)

print(f'Area: {paralelograma.calcular_area()}')
print(f'Perimetro: {paralelograma.calcular_perimetro()}')
