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

type Felino struct{}

func (f Felino) EmitirSom() string {
	return "Miau"
}

func ProduzirSom(sv SerVivo) {
	fmt.Println(sv.EmitirSom())
}

func main() {
	var animalCao SerVivo = Cão{}
	var animalGato SerVivo = Felino{}

	ProduzirSom(animalCao)
	ProduzirSom(animalGato)
}
