package main

import (
	"fmt"
)

type Conta struct {
	NomeTitular string
	Saldo       float64
}

func (c *Conta) AdicionarValor(valor float64) {
	if valor > 0 {
		c.Saldo += valor
	}
}

func (c *Conta) RemoverValor(valor float64) bool {
	if valor > 0 && valor <= c.Saldo {
		c.Saldo -= valor
		return true
	}
	return false
}

func (c Conta) ConsultarSaldo() float64 {
	return c.Saldo
}

func main() {
	contaA := Conta{NomeTitular: "João"}
	contaB := Conta{NomeTitular: "Maria"}

	contaA.AdicionarValor(500)
	contaB.AdicionarValor(300)

	fmt.Printf("Saldo de %s: %.2f\n", contaA.NomeTitular, contaA.ConsultarSaldo())
	fmt.Printf("Saldo de %s: %.2f\n", contaB.NomeTitular, contaB.ConsultarSaldo())

	if contaA.RemoverValor(200) {
		fmt.Printf("Saque de 200 realizado com sucesso.\n")
	} else {
		fmt.Printf("Saque de 200 não pode ser realizado.\n")
	}

	fmt.Printf("Saldo de %s após o saque: %.2f\n", contaA.NomeTitular, contaA.ConsultarSaldo())
}
