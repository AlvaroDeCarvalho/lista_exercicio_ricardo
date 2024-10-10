class Funcionario:
    def __init__(self, nome_funcionario, cargo_funcionario, salario_funcionario):
        self.nome_funcionario = nome_funcionario
        self.cargo_funcionario = cargo_funcionario
        self.salario_funcionario = salario_funcionario

    def mostrar_detalhes(self):
        return f"Nome: {self.nome_funcionario}, Cargo: {self.cargo_funcionario}, Salário: R${self.salario_funcionario:.2f}"

class Organizacao:
    def __init__(self, nome_organizacao):
        self.nome_organizacao = nome_organizacao
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def mostrar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.mostrar_detalhes())

def executar():
    organizacao = Organizacao("Soluções Tecnológicas")

    funcionario1 = Funcionario("Carlos Silva", "Desenvolvedor", 5000)
    funcionario2 = Funcionario("Ana Souza", "Gerente de Projetos", 8000)
    funcionario3 = Funcionario("João Oliveira", "Analista de Sistemas", 6000)

    organizacao.adicionar_funcionario(funcionario1)
    organizacao.adicionar_funcionario(funcionario2)
    organizacao.adicionar_funcionario(funcionario3)

    print(f"Funcionários da organização {organizacao.nome_organizacao}:")
    organizacao.mostrar_funcionarios()

if __name__ == "__main__":
    executar()
