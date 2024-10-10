class Calculadora:
    @staticmethod
    def fatorial(valor):
        if valor < 0:
            raise ValueError("O fatorial não está definido para números negativos.")
        elif valor == 0 or valor == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, valor + 1):
                resultado *= i
            return resultado

def executar():
    numero = 5
    resultado_fatorial = Calculadora.fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado_fatorial}")

    try:
        fatorial_negativo = Calculadora.fatorial(-3)
    except ValueError as erro:
        print(erro)

if __name__ == "__main__":
    executar()
