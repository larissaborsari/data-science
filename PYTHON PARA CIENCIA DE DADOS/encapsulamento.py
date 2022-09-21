#proteção aos dados de um objeto
#recursos públicos e privados

#publico - pode ser acessado fora da classe
# privado - só pode ser acessado pela classe

class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo= saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        #... verificar se o depósito pode ser realizado
        self._saldo += valor
    
    def sacar(self, valor):
        #... verificar se o saque pode ser realizado
        self._saldo -= valor
    
    def exibir_saldo(self):
        #... verificar se a pessoa pode ver o saldo
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.exibir_saldo())