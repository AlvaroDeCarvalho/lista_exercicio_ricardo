package main

import (
	"fmt"
)

type Docente struct {
	Nome        string
	Disciplinas []string
}

type Instituicao struct {
	Nome     string
	Docentes []*Docente // Lista de ponteiros para Docentes
}

func (i *Instituicao) AdicionarDocente(d *Docente) {
	i.Docentes = append(i.Docentes, d)
}

func (d *Docente) Ensinar() {
	fmt.Printf("Docente %s ensina as disciplinas: %v\n", d.Nome, d.Disciplinas)
}

func main() {
	instituicao1 := Instituicao{Nome: "Instituição A"}
	instituicao2 := Instituicao{Nome: "Instituição B"}

	docente1 := &Docente{Nome: "Carlos", Disciplinas: []string{"Matemática", "Física"}}
	docente2 := &Docente{Nome: "Maria", Disciplinas: []string{"Português", "Literatura"}}
	docente3 := &Docente{Nome: "João", Disciplinas: []string{"Química", "Biologia"}}

	instituicao1.AdicionarDocente(docente1)
	instituicao1.AdicionarDocente(docente2)

	instituicao2.AdicionarDocente(docente2)
	instituicao2.AdicionarDocente(docente3)

	fmt.Printf("Docentes da %s:\n", instituicao1.Nome)
	for _, doc := range instituicao1.Docentes {
		doc.Ensinar()
	}

	fmt.Printf("\nDocentes da %s:\n", instituicao2.Nome)
	for _, doc := range instituicao2.Docentes {
		doc.Ensinar()
	}
}
