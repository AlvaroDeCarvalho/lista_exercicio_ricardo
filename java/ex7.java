public class ex7 {
    class Motor {
        private String tipo; 
        private int potencia; 
    
        public Motor(String tipo, int potencia) {
            this.tipo = tipo;
            this.potencia = potencia;
        }
    
        public String getTipo() {
            return tipo;
        }
    
        public int getPotencia() {
            return potencia;
        }
    
        public void mostrarDetalhes() {
            System.out.println("Motor tipo: " + tipo + ", Potência: " + potencia + " CV");
        }
    }
    
    class Veiculo {
        private String marca;
        private String modelo;
        private int ano;
        private Motor motor; 
    
        public Veiculo(String marca, String modelo, int ano, Motor motor) {
            this.marca = marca;
            this.modelo = modelo;
            this.ano = ano;
            this.motor = motor; 
        }
    
        public void mostrarDetalhes() {
            System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
            motor.mostrarDetalhes(); 
        }
    
        public static void main(String[] args) {
            
            ex7 outer = new ex7();
            Motor motor1 = outer.new Motor("Gasolina", 120);
    
            Veiculo veiculo1 = outer.new Veiculo("Toyota", "Corolla", 2020, motor1);
    
            veiculo1.mostrarDetalhes();
        }
    }
    
}
