class Educador:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []  

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_educador(self)  

    def mostrar_escolas(self):
        return ", ".join([escola.nome for escola in self.escolas])

class Instituicao:
    def __init__(self, nome):
        self.nome = nome
        self.educadores = []  

    def adicionar_educador(self, educador):
        if educador not in self.educadores:
            self.educadores.append(educador)

    def mostrar_educadores(self):
        return ", ".join([educador.nome for educador in self.educadores])


def executar():
    instituicao1 = Instituicao("Escola Primária")
    instituicao2 = Instituicao("Escola Secundária")

    educador1 = Educador("Carlos")
    educador2 = Educador("Ana")

    educador1.adicionar_escola(instituicao1)
    educador1.adicionar_escola(instituicao2)
    educador2.adicionar_escola(instituicao1)

    print(f"{educador1.nome} leciona em: {educador1.mostrar_escolas()}")
    print(f"{educador2.nome} leciona em: {educador2.mostrar_escolas()}")

    print(f"Educadores da {instituicao1.nome}: {instituicao1.mostrar_educadores()}")
    print(f"Educadores da {instituicao2.nome}: {instituicao2.mostrar_educadores()}")


if __name__ == "__main__":
    executar()
