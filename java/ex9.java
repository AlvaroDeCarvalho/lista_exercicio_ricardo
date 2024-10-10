public class ex9 {
    interface Imprimivel {
        void imprimir();
    }
    
    class Relatorio implements Imprimivel {
        public void imprimir() {
            System.out.println("Imprimindo relatório...");
        }
    }
    
    class Contrato implements Imprimivel {
        public void imprimir() {
            System.out.println("Imprimindo contrato...");
        }
    }
    
}
