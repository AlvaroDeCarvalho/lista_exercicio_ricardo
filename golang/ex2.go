package main

import (
	"fmt"
)

type Automovel struct {
	Marca      string
	Model      string
	Ano        int
	Velocidade int
}

func (a *Automovel) Acelerar(quantidade int) {
	a.Velocidade += quantidade
}

func (a *Automovel) DiminuirVelocidade(quantidade int) {
	if a.Velocidade-quantidade < 0 {
		a.Velocidade = 0
	} else {
		a.Velocidade -= quantidade
	}
}

func (a Automovel) MostrarVelocidade() {
	fmt.Printf("A velocidade atual do %s %s é: %d km/h\n", a.Marca, a.Model, a.Velocidade)
}

func main() {

	veiculo1 := Automovel{Marca: "Toyota", Model: "Corolla", Ano: 2020}
	veiculo2 := Automovel{Marca: "Ford", Model: "Focus", Ano: 2019}
	veiculo3 := Automovel{Marca: "Honda", Model: "Civic", Ano: 2021}

	veiculo1.Acelerar(50)
	veiculo1.MostrarVelocidade()

	veiculo2.Acelerar(30)
	veiculo2.MostrarVelocidade()

	veiculo3.Acelerar(70)
	veiculo3.MostrarVelocidade()

	veiculo1.DiminuirVelocidade(20)
	veiculo1.MostrarVelocidade()

	veiculo2.DiminuirVelocidade(50)
	veiculo2.MostrarVelocidade()

	veiculo3.DiminuirVelocidade(100)
	veiculo3.MostrarVelocidade()
}
