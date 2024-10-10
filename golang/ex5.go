package main

import (
	"fmt"
)

type SerVivo interface {
	EmitirSom() string
}

type Cão struct{}

func (c Cão) EmitirSom() string {
	return "Au Au"
}

type Gato struct{}

func (g Gato) EmitirSom() string {
	return "Miau"
}

func ProduzirSons(seres []SerVivo) {
	for _, ser := range seres {
		fmt.Println(ser.EmitirSom())
	}
}

func main() {
	animalCao := Cão{}
	animalGato := Gato{}

	seres := []SerVivo{animalCao, animalGato}

	ProduzirSons(seres)
}
