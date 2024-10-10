package main

import (
	"fmt"
)

type Item struct {
	Nome  string
	Preco float64
}

func SomarItens(i1, i2 Item) Item {
	return Item{
		Nome:  i1.Nome + " e " + i2.Nome,
		Preco: i1.Preco + i2.Preco,
	}
}

func main() {
	item1 := Item{Nome: "Item A", Preco: 30.50}
	item2 := Item{Nome: "Item B", Preco: 20.75}

	resultado := SomarItens(item1, item2)

	fmt.Printf("Item: %s\nPreço Total: %.2f\n", resultado.Nome, resultado.Preco)
}
