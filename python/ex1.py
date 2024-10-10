class Veiculo:
    def __init__(self, fabricante, tipo, ano_fabricacao):
        self.fabricante = fabricante
        self.tipo = tipo
        self.ano_fabricacao = ano_fabricacao

    def mostrar_informacoes(self):
        return f"Fabricante: {self.fabricante}, Tipo: {self.tipo}, Ano: {self.ano_fabricacao}"


def executar():
    veiculo1 = Veiculo("Toyota", "Corolla", 2024)
    veiculo2 = Veiculo("BMW", "X6", 2023)
    veiculo3 = Veiculo("Chevrolet", "Montana", 2015)

    print(veiculo1.mostrar_informacoes())
    print(veiculo2.mostrar_informacoes())
    print(veiculo3.mostrar_informacoes())


if __name__ == "__main__":
    executar()
