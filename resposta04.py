# Classe Pessoa: Crie uma classe que modele uma pessoa:
# A. Atributos: nome, idade, peso e altura
# B. Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade
# dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def engordar(self, peso):
        if peso > self.__peso:
            self.__peso = peso

    def emagrecer(self, peso):
        if peso < self.__peso:
            self.__peso = peso
        else:
            self.engordar()

    def crescer(self, altura):
        self.__altura = altura

    def envelhecer(self, nova_idade):
        anos = nova_idade - self.__idade
        print(anos)
        self.__idade = nova_idade
        if nova_idade < 21:
            self.crescer(self.__altura + anos * 0.005)
    #    else:
    #        self.crescer((21-nova_idade)*0,5)

# Teste da classe Pessoa

# nome = input('Digite nome: ')
# idade = int(input('Digite a idade: '))
# peso = float(input('Digite o peso: '))
# altura = float(input('Digite a altura: '))
# print("Altura = %.2f" %(altura))

p1 = Pessoa('José',16, 56, 1.70)
print(f'Nome: {p1._Pessoa__nome} Idade: {p1._Pessoa__idade} Peso: {p1._Pessoa__peso} Altura: {p1._Pessoa__altura}')

p1.envelhecer(18)
print(f'Nome: {p1._Pessoa__nome} Idade: {p1._Pessoa__idade} Peso: {p1._Pessoa__peso} Altura: {p1._Pessoa__altura}')
