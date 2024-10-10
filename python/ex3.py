class ContaBancaria:
    def __init__(self, cliente, saldo_inicial=0):
        self.__saldo_atual = saldo_inicial  
        self.cliente = cliente

    def adicionar_deposito(self, valor):
        if valor > 0:
            self.__saldo_atual += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def realizar_saque(self, valor):
        if valor > 0:
            if valor <= self.__saldo_atual:
                self.__saldo_atual -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor de saque deve ser positivo.")

    def mostrar_saldo(self):
        return f"Saldo atual: R${self.__saldo_atual:.2f}"


def executar():
    conta_cliente = ContaBancaria("Leonardo Sobrinho", 1000)
    
    print(conta_cliente.mostrar_saldo())
    
    conta_cliente.adicionar_deposito(500)
    print(conta_cliente.mostrar_saldo())
    
    conta_cliente.realizar_saque(300)
    print(conta_cliente.mostrar_saldo())
    
    conta_cliente.realizar_saque(1500)  


if __name__ == "__main__":
    executar()
