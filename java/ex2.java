class Veiculo {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade; 

    public Veiculo(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0; 
    }

    public void acelerar(int incremento) {
        this.velocidade += incremento;
        System.out.println("Acelerando. Velocidade atual: " + this.velocidade + " km/h");
    }

    public void frear(int decremento) {
        this.velocidade -= decremento;
        if (this.velocidade < 0) {
            this.velocidade = 0; 
        }
        System.out.println("Freando. Velocidade atual: " + this.velocidade + " km/h");
    }

    public void mostrarVelocidade() {
        System.out.println("Velocidade atual: " + this.velocidade + " km/h");
    }

    public void mostrarDetalhes() {
        System.out.println("Marca: " + this.marca + ", Modelo: " + this.modelo + ", Ano: " + this.ano);
    }

    public static void main(String[] args) {
        
        Veiculo veiculo1 = new Veiculo("Toyota", "Corolla", 2020);
        Veiculo veiculo2 = new Veiculo("Honda", "Civic", 2021);
        Veiculo veiculo3 = new Veiculo("Ford", "Focus", 2019);

        veiculo1.mostrarDetalhes();
        veiculo2.mostrarDetalhes();
        veiculo3.mostrarDetalhes();

        veiculo1.acelerar(50);
        veiculo1.frear(20);
        veiculo1.mostrarVelocidade();
        veiculo1.frear(40); 
    }
}
