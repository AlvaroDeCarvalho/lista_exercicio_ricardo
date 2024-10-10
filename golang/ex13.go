package main

import (
	"fmt"
)

type Calculadora struct{}

func (Calculadora) Fatorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * Calculadora{}.Fatorial(n-1)
}

func main() {
	calculadora := Calculadora{}
	numero := 5
	resultado := calculadora.Fatorial(numero)
	fmt.Printf("Fatorial de %d é %d\n", numero, resultado)
}
