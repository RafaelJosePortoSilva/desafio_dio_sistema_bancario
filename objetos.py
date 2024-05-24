from abc import ABC, abstractmethod
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
        return aux



class Historico:
    def __init__(self):
        self.dados = []

    def adicionar_transacao(self,transacao,conta):
        self.dados.append(transacao,conta)


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        ...

class Deposito(Transacao):

    def __init__(self,valor):
        self.valor = valor
    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)
        ...

class Cliente:

    def __init__(self,endereco,contas=[]):
        self.endereco=endereco
        self.contas=contas

    def adicionar_transacao(self, conta, transacao):
        Historico().adicionar_transacao(transacao,conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self,endereco, cpf, nome, data_nascimento ,contas=[]):
        super().__init__(endereco,contas)

        self.cpf=cpf
        self.nome=nome
        self.data_nascimentp=data_nascimento