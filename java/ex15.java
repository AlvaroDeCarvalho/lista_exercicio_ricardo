public class ex15 {
    static class ExcecaoSaldoInsuficiente extends Exception {
        public ExcecaoSaldoInsuficiente(String mensagem) {
            super(mensagem);
        }
    }
    
    static class ContaCorrente {
        private double saldo;
        private String titular;
    
        public ContaCorrente(String titular, double saldoInicial) {
            this.titular = titular;
            this.saldo = saldoInicial;
        }
    
        public void depositar(double valor) {
            saldo += valor;
        }
    
        public void sacar(double valor) throws ExcecaoSaldoInsuficiente {
            if (valor > saldo) {
                throw new ExcecaoSaldoInsuficiente("Saldo insuficiente para realizar o saque.");
            }
            saldo -= valor;
        }
    
        public double obterSaldo() {
            return saldo;
        }
    
        public String obterTitular() {
            return titular;
        }
    }
    
    public class Main {
        public static void main(String[] args) {
            ContaCorrente conta = new ContaCorrente("João", 1000.00);
    
            try {
                conta.sacar(1500.00);
            } catch (ExcecaoSaldoInsuficiente e) {
                System.out.println(e.getMessage());
            }
    
            conta.depositar(500.00);
            try {
                conta.sacar(1500.00);
            } catch (ExcecaoSaldoInsuficiente e) {
                System.out.println(e.getMessage());
            }
    
            System.out.println("Saldo atual: R$ " + conta.obterSaldo());
        }
    }
    
}
