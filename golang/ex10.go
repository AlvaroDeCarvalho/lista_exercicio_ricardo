package main

import (
	"fmt"
)

type Computador struct{}

func (c Computador) SomarDuasValores(x, y float64) float64 {
	return x + y
}

func (c Computador) SomarTresValores(x, y, z float64) float64 {
	return x + y + z
}

func main() {
	computador := Computador{}

	resultado1 := computador.SomarDuasValores(5.5, 3.2)
	fmt.Printf("Resultado da soma de dois valores: %.2f\n", resultado1)

	resultado2 := computador.SomarTresValores(4.0, 2.5, 1.5)
	fmt.Printf("Resultado da soma de três valores: %.2f\n", resultado2)
}
