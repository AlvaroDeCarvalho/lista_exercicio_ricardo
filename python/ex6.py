class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def mostrar_potencia(self):
        return f"Potência do motor: {self.potencia} CV"


class Veiculo:
    def __init__(self, fabricante, modelo, ano, motor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.motor = motor  

    def mostrar_detalhes(self):
        return (f"Fabricante: {self.fabricante}, Modelo: {self.modelo}, Ano: {self.ano}, "
                f"{self.motor.mostrar_potencia()}")


def executar():
    motor_v8 = Motor(450)  
    veiculo1 = Veiculo("Ford", "Mustang", 2022, motor_v8)  

    print(veiculo1.mostrar_detalhes())


if __name__ == "__main__":
    executar()
