# Classe Bichinho Virtual:
# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade
# Métodos: Alterar Nome, Fome, Saúde e Idade;
# Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do
# nosso tamagushi, este humor é uma combinação entre os atributos
# Fome e Saúde, ou seja, um campo calculado, então não devemos criar
# um atributo para armazenar esta informação por que ela pode ser
# calculada a qualquer momento



class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade= 0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def alterar_nome(self, nome):
        self.__nome = nome

    def alterar_fome(self, fome):
        self.__fome = fome

    def alterar_saude(self, saude):
        self.__saude = saude

    def alterar_idade(self, idade):
        self.__idade = idade

    def humor(self):
        humor = self.__fome == 'sim' or self.__saude == 'não'
        if humor:
            return f'Cuidado! {self.__nome} está zangado'
        return f'Brinque muito, {self.__nome} está feliz!'

    #Se eu não criar esta função, o Python imprime a posição da memória onde está o objeto
    def __str__(self):
        return f'Nome: {self.__nome}, fome: {self.__fome}, saúde: {self.__saude}, idade: {self.__idade} anos'

# Teste da classe BichinhoVirtual

# Posso atribuir valor do tipo lógico a um atributo, porém ficou estranho
# tomaguchi = BichinhoVirtual('Bidu',True,False,2)

tomaguchi = BichinhoVirtual('Bidu','sim','não',2)
print(tomaguchi)

tomaguchi.alterar_nome('Bob')
print(tomaguchi.humor(),'\n')

tomaguchi.alterar_fome('não')
print(tomaguchi)
print(tomaguchi.humor(),'\n')

tomaguchi.alterar_saude('sim')
print(tomaguchi)
print(tomaguchi.humor(),'\n')
