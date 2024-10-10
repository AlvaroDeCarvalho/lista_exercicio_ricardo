package main

import (
	"fmt"
)

type Colaborador struct {
	Nome    string
	Cargo   string
	Salario float64
}

type Organizacao struct {
	Nome        string
	Colaboradores []Colaborador // Lista de colaboradores
}

func (o *Organizacao) AdicionarColaborador(col Colaborador) {
	o.Colaboradores = append(o.Colaboradores, col)
}

func (o *Organizacao) ExibirColaboradores() {
	fmt.Printf("Colaboradores da organização %s:\n", o.Nome)
	for _, col := range o.Colaboradores {
		fmt.Printf("Nome: %s, Cargo: %s, Salário: %.2f\n", col.Nome, col.Cargo, col.Salario)
	}
}

func main() {
	organizacao := Organizacao{Nome: "Tech Solutions"}

	colab1 := Colaborador{Nome: "Ana", Cargo: "Desenvolvedora", Salario: 5000.00}
	colab2 := Colaborador{Nome: "Bruno", Cargo: "Gerente de Projetos", Salario: 8000.00}
	colab3 := Colaborador{Nome: "Carla", Cargo: "Analista de Sistemas", Salario: 6000.00}

	organizacao.AdicionarColaborador(colab1)
	organizacao.AdicionarColaborador(colab2)
	organizacao.AdicionarColaborador(colab3)

	organizacao.ExibirColaboradores()
}
