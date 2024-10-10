package main

import (
	"fmt"
)

type ErroSaldoInsuficiente struct {
	Saldo float64
	Valor float64
}

func (e *ErroSaldoInsuficiente) Error() string {
	return fmt.Sprintf("saldo insuficiente: saldo atual é %.2f, tentativa de saque de %.2f", e.Saldo, e.Valor)
}

type ContaCorrente struct {
	Saldo float64
}

func (c *ContaCorrente) Sacar(valor float64) error {
	if valor > c.Saldo {
		return &ErroSaldoInsuficiente{Saldo: c.Saldo, Valor: valor}
	}
	c.Saldo -= valor
	return nil
}

func main() {
	conta := ContaCorrente{Saldo: 100.0}

	err := conta.Sacar(150.0)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("Saque realizado com sucesso. Novo saldo: %.2f\n", conta.Saldo)
	}
}
