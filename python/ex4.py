class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        raise NotImplementedError("Método deve ser sobrescrito pelas subclasses")


class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} faz: Au Au!"


class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} faz: Miau!"


def executar():
    cachorro = Cachorro("Tobby")
    gato = Gato("Luana")

    print(cachorro.emitir_som())
    print(gato.emitir_som())


if __name__ == "__main__":
    executar()
