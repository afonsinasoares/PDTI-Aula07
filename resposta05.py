# Classe Conta Corrente: Crie uma classe para implementar uma conta
# corrente. A classe deve possuir os seguintes atributos: número da conta,
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
# depósito e saque; No construtor, saldo é opcional, com valor default zero
# e os demais atributos são obrigatórios.

class ContaCorrente:

    def __init__(self, numero, correntista, saldo = 0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    def mudar_correntista(self, correntista):
        self.correntista = correntista

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor deve ser maior que zero')

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo Insuficiente')

  
# Teste da classe ContaCorrente
conta_maria = ContaCorrente(111, 'Maria')

conta_paulo = ContaCorrente(222, 'Paulo', 1000.0)

conta_maria.sacar(200.0)
conta_maria.depositar(2000.0)
conta_maria.sacar(500.0)
print(conta_maria.saldo) #é possível fazer assim porque o saldo não está privado
