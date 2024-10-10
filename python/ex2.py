class Veiculo:
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0  

    def mostrar_informacoes(self):
        return f"Fabricante: {self.fabricante}, Modelo: {self.modelo}, Ano: {self.ano}"

    def acelerar(self, incremento):
        self.velocidade_atual += incremento
        print(f"O veículo acelerou {incremento} km/h. Velocidade atual: {self.velocidade_atual} km/h")

    def frear(self, decremento):
        self.velocidade_atual = max(0, self.velocidade_atual - decremento)  
        print(f"O veículo reduziu {decremento} km/h. Velocidade atual: {self.velocidade_atual} km/h")

    def mostrar_velocidade(self):
        return f"Velocidade atual: {self.velocidade_atual} km/h"


if __name__ == "__main__":
    veiculo1 = Veiculo("Toyota", "Corolla", 2020)
    
    print(veiculo1.mostrar_informacoes())
    
    veiculo1.acelerar(20)
    veiculo1.acelerar(30)
    veiculo1.frear(10)
    print(veiculo1.mostrar_velocidade())
    veiculo1.frear(50)
    print(veiculo1.mostrar_velocidade())
