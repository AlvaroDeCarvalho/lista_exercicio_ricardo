from abc import ABC, abstractmethod


class Empregado(ABC):
    @abstractmethod
    def calcular_remuneracao(self):
        pass


class EmpregadoHorista(Empregado):
    def __init__(self, nome_empregado, horas_trabalhadas, valor_por_hora):
        self.nome_empregado = nome_empregado
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_remuneracao(self):
        return self.horas_trabalhadas * self.valor_por_hora


class EmpregadoAssalariado(Empregado):
    def __init__(self, nome_empregado, salario_mensal):
        self.nome_empregado = nome_empregado
        self.salario_mensal = salario_mensal

    def calcular_remuneracao(self):
        return self.salario_mensal


def executar():
    empregado_horista = EmpregadoHorista("Carlos", 40, 15)  # 40 horas trabalhadas a R$15/h
    empregado_assalariado = EmpregadoAssalariado("Ana", 3000)  # Salário fixo de R$3000

    print(f"Remuneração do {empregado_horista.nome_empregado}: R${empregado_horista.calcular_remuneracao():.2f}")
    print(f"Remuneração da {empregado_assalariado.nome_empregado}: R${empregado_assalariado.calcular_remuneracao():.2f}")


if __name__ == "__main__":
    executar()
