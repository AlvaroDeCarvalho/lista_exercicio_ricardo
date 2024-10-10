from abc import ABC, abstractmethod


class Colaborador(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass


class ColaboradorHorista(Colaborador):
    def __init__(self, nome_colaborador, horas_trabalhadas, valor_por_hora):
        self.nome_colaborador = nome_colaborador
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora


class ColaboradorAssalariado(Colaborador):
    def __init__(self, nome_colaborador, salario_mensal):
        self.nome_colaborador = nome_colaborador
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal


def rodar():
    colaborador_horista = ColaboradorHorista("Carlos", 40, 15)  # 40 horas trabalhadas a R$15/h
    colaborador_assalariado = ColaboradorAssalariado("Ana", 3000)  # Salário fixo de R$3000

    print(f"Salário do {colaborador_horista.nome_colaborador}: R${colaborador_horista.calcular_salario():.2f}")
    print(f"Salário da {colaborador_assalariado.nome_colaborador}: R${colaborador_assalariado.calcular_salario():.2f}")


if __name__ == "__main__":
    rodar()
