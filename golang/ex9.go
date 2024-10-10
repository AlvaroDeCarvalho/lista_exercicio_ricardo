package main

import (
	"fmt"
)

type Exibível interface {
	Exibir()
}

type Relatorio struct {
	Titulo   string
	Conteudo string
}

func (r Relatorio) Exibir() {
	fmt.Printf("Relatório: %s\nConteúdo: %s\n", r.Titulo, r.Conteudo)
}

type Contrato struct {
	Partes string
	Termos string
}

func (c Contrato) Exibir() {
	fmt.Printf("Contrato entre: %s\nTermos: %s\n", c.Partes, c.Termos)
}

func ExibirDocumento(e Exibível) {
	e.Exibir()
}

func main() {
	relatorio := Relatorio{Titulo: "Relatório Anual", Conteudo: "Este é o conteúdo do relatório anual."}
	contrato := Contrato{Partes: "Empresa A e Empresa B", Termos: "Os termos do contrato são..."}

	ExibirDocumento(relatorio)
	ExibirDocumento(contrato)
}
