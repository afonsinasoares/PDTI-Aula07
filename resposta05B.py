# Igual a resposta05
# Agora com transferência
class ContaCorrente:

    def __init__(self, numero, correntista, saldo=0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    def mudar_correntista(self, correntista):
        self.correntista = correntista

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            return destino.depositar(valor)
        return False

# Teste da classe ContaCorrente
conta_maria = ContaCorrente(111, 'Maria')

conta_paulo = ContaCorrente(222, 'Paulo', 1000.0)

# Paulo tem saldo para fazer a transferência
conta_paulo.transferir(100.0, conta_maria)
print(f'Paulo: {conta_paulo.saldo}')
print(f'Maria: {conta_maria.saldo} \n') #'\n' quebra linha

# Maria não tem saldo suficiente
# teste condicional e mensagem
if not conta_maria.transferir(200.0, conta_paulo):
    print('Transferência não efetivada por falta de saldo!')
print(f'Paulo: {conta_paulo.saldo}')
print(f'Maria: {conta_maria.saldo}')