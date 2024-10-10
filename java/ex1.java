class Veiculo {
    private String marca;
    private String modelo;
    private int ano;

    public Veiculo(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
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
    }
}
