public class ex3 {
    class ContaBancaria {
        private double saldo;
        public String titular;
    
        public ContaBancaria(String titular, double saldo) {
            this.titular = titular;
            this.saldo = saldo;
        }
    
        public void depositar(double valor) {
            if (valor > 0) {
                saldo += valor;
            }
        }
    
        public void sacar(double valor) throws SaldoInsuficienteException {
            if (valor > 0 && valor <= saldo) {
                saldo -= valor;
            } else {
                throw new SaldoInsuficienteException("Saldo insuficiente");
            }
        }
    
        public String exibirSaldo() {
            return "Saldo: " + saldo;
        }
    
        public static void main(String[] args) {
            try {
                ex3 outer = new ex3();
                ContaBancaria conta = outer.new ContaBancaria("João", 100);
                conta.depositar(50);
                System.out.println(conta.exibirSaldo());  // Saldo: 150
                conta.sacar(30);
                System.out.println(conta.exibirSaldo());  // Saldo: 120
            } catch (SaldoInsuficienteException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    class SaldoInsuficienteException extends Exception {
        public SaldoInsuficienteException(String mensagem) {
            super(mensagem);
        }
    }
}
