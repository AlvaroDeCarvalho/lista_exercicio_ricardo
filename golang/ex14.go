package main

import (
	"fmt"
	"sync"
)

type Config struct {
	Parametro string
}

var instance *Config
var once sync.Once

func GetConfig() *Config {
	once.Do(func() {
		instance = &Config{Parametro: "Valor padrão"}
	})
	return instance
}

func main() {
	config1 := GetConfig()
	fmt.Println("Configuração 1:", config1.Parametro)

	config2 := GetConfig()
	config2.Parametro = "Novo valor"

	fmt.Println("Configuração 1 após alteração:", config1.Parametro)
	fmt.Println("Configuração 2:", config2.Parametro)
}
