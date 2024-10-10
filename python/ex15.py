class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para a operação."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class ContaCorrente:
    def __init__(self, titular_conta, saldo_inicial=0):
        self.titular_conta = titular_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Tentativa de saque: R${valor:.2f}. Saldo disponível: R${self.saldo:.2f}")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")


def executar():
    conta_corrente = ContaCorrente("João", 100)

    try:
        conta_corrente.sacar(150)  
    except SaldoInsuficienteError as erro:
        print(erro)

    conta_corrente.depositar(50)  
    try:
        conta_corrente.sacar(100)  
    except SaldoInsuficienteError as erro:
        print(erro)

if __name__ == "__main__":
    executar()
