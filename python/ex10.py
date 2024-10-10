class Adicionadora:
    def adicionar(self, *valores):
        return sum(valores)


def executar():
    calculadora = Adicionadora()

    resultado_2 = calculadora.adicionar(5, 10)
    print(f"Soma de 5 e 10: {resultado_2}")

    resultado_3 = calculadora.adicionar(5, 10, 15)
    print(f"Soma de 5, 10 e 15: {resultado_3}")


if __name__ == "__main__":
    executar()
