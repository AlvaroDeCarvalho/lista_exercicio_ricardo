package main

import (
	"fmt"
)

type Propulsor struct {
	Potencia int    // Potência do motor em cavalos de potência (CV)
	Tipo     string // Tipo de motor (ex: "Gasolina", "Álcool", "Elétrico")
}

type Veiculo struct {
	Marca  string
	Modelo string
	Ano    int
	Propulsor Propulsor // Associando um objeto Propulsor à classe Veiculo
}

func main() {
	propulsor1 := Propulsor{Potencia: 150, Tipo: "Gasolina"}
	veiculo1 := Veiculo{Marca: "Toyota", Modelo: "Corolla", Ano: 2020, Propulsor: propulsor1}

	propulsor2 := Propulsor{Potencia: 200, Tipo: "Elétrico"}
	veiculo2 := Veiculo{Marca: "Tesla", Modelo: "Model 3", Ano: 2021, Propulsor: propulsor2}

	fmt.Printf("Veículo: %s %s (%d) - Propulsor: %d CV, Tipo: %s\n", veiculo1.Marca, veiculo1.Modelo, veiculo1.Ano, veiculo1.Propulsor.Potencia, veiculo1.Propulsor.Tipo)
	fmt.Printf("Veículo: %s %s (%d) - Propulsor: %d CV, Tipo: %s\n", veiculo2.Marca, veiculo2.Modelo, veiculo2.Ano, veiculo2.Propulsor.Potencia, veiculo2.Propulsor.Tipo)
}
