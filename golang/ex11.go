package main

import (
	"fmt"
)

type Empregado interface {
	CalcularSalario() float64
}

type EmpregadoHorista struct {
	HorasTrabalhadas float64
	ValorHora        float64
}

func (e EmpregadoHorista) CalcularSalario() float64 {
	return e.HorasTrabalhadas * e.ValorHora
}

type EmpregadoAssalariado struct {
	SalarioMensal float64
}

func (e EmpregadoAssalariado) CalcularSalario() float64 {
	return e.SalarioMensal
}

func ExibirSalario(emp Empregado) {
	fmt.Printf("Salário: %.2f\n", emp.CalcularSalario())
}

func main() {
	empregado1 := EmpregadoHorista{HorasTrabalhadas: 40, ValorHora: 15.0}
	empregado2 := EmpregadoAssalariado{SalarioMensal: 3000.0}

	ExibirSalario(empregado1)
	ExibirSalario(empregado2)
}
