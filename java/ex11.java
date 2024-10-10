public class ex11 {
    abstract class Funcionario {
        public abstract double calcularSalario();
    }
    
    class FuncionarioHorista extends Funcionario {
        private double valorPorHora;
        private int horasTrabalhadas;
    
        public FuncionarioHorista(double valorPorHora, int horasTrabalhadas) {
            this.valorPorHora = valorPorHora;
            this.horasTrabalhadas = horasTrabalhadas;
        }
    
        @Override
        public double calcularSalario() {
            return valorPorHora * horasTrabalhadas;
        }
    }
    
    class FuncionarioAssalariado extends Funcionario {
        private double salarioMensal;
    
        public FuncionarioAssalariado(double salarioMensal) {
            this.salarioMensal = salarioMensal;
        }
    
        @Override
        public double calcularSalario() {
            return salarioMensal;
        }
    }
    
}
