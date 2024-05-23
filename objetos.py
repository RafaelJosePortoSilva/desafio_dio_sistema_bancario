from abc import ABC
class Conta:

    def __init__(self,numero,agencia,cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def get_saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls,numero,agencia,cliente):
        return cls(numero,agencia,cliente)

    def sacar(self,valor):
        if valor <= self.get_saldo() and valor > 0:
            self._saldo -= valor
            return f'Saque efetuado'
        else:
            return f'Saque não foi feito'

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor


class ContaCorrente(Conta):

    def set_limite(self,limite):
        self.limite = limite
        return f'Limite alterado'

    def set_limite_saques(self,limite):
        self.limite_saque = limite
        return f'Limite de saques alterado'

    @classmethod
    def nova_conta(cls,numero,agencia,cliente, limite=300, limite_saques=3):
        aux = ContaCorrente(numero, agencia, cliente)
        aux.set_limite(limite)
        aux.set_limite_saques(limite_saques)



class Historico:
    def __init__(self):
        self.dados = []

    def adicionar_transacao(self,transacao):
        self.dados.append(transacao)

class Transacao(ABC):
    ...

class Deposito(Transacao):
    ...

class Saque(Transacao):
    ...

class Cliente:
    ...

class PessoaFisica(Cliente):
    ...