class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses")


class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} faz: Au Au!"


class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} faz: Miau!"


def fazer_animais_emitir_sons(lista_animais):
    for animal in lista_animais:
        print(animal.emitir_som())


def executar():
    cachorro1 = Cachorro("Rex")
    gato1 = Gato("Mimi")
    cachorro2 = Cachorro("Bolt")

    lista_animais = [cachorro1, gato1, cachorro2]

    fazer_animais_emitir_sons(lista_animais)


if __name__ == "__main__":
    executar()
