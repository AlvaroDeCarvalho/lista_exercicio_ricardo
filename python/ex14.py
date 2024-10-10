class ConfiguracaoGlobal:
    _instancia = None  

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConfiguracaoGlobal, cls).__new__(cls)
            cls._instancia.configuracoes = {}
        return cls._instancia

    def definir_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor

    def obter_configuracao(self, chave):
        return self.configuracoes.get(chave, None)


def executar():
    configuracao1 = ConfiguracaoGlobal()
    configuracao2 = ConfiguracaoGlobal()

    configuracao1.definir_configuracao("tema", "escuro")
    print(f"Configuração do tema: {configuracao2.obter_configuracao('tema')}")  # Deve mostrar "escuro"

    # Verifica se ambas as variáveis são a mesma instância
    print(f"Configuração1 é a mesma que Configuração2? {configuracao1 is configuracao2}")


if __name__ == "__main__":
    executar()
