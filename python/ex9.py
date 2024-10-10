from abc import ABC, abstractmethod


class Documento(ABC):
    @abstractmethod
    def mostrar(self):
        pass


class RelatorioFinanceiro(Documento):
    def __init__(self, dados):
        self.dados = dados

    def mostrar(self):
        print(f"Mostrando Relatório Financeiro: {self.dados}")


class Acordo(Documento):
    def __init__(self, envolvidos):
        self.envolvidos = envolvidos

    def mostrar(self):
        print(f"Mostrando Acordo entre: {', '.join(self.envolvidos)}")


def executar():
    relatorio_financeiro = RelatorioFinanceiro("Análise de Desempenho 2024")
    acordo = Acordo(["Empresa A", "Empresa B"])

    relatorio_financeiro.mostrar()
    acordo.mostrar()


if __name__ == "__main__":
    executar()
