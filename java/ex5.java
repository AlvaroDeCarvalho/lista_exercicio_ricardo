class ContaCorrente {
    private String titular;
    private double saldo; 

    public ContaCorrente(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial; 
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.printf("Depósito de R$%.2f realizado com sucesso. Saldo atual: R$%.2f%n", valor, saldo);
        } else {
            System.out.println("Valor de depósito deve ser positivo.");
        }
    }

    public void sacar(double valor) {
        if (valor > saldo) {
            System.out.println("Saque não realizado. Saldo insuficiente.");
        } else {
            saldo -= valor;
            System.out.printf("Saque de R$%.2f realizado com sucesso. Saldo atual: R$%.2f%n", valor, saldo);
        }
    }

    public double getSaldo() {
        return saldo;
    }

    public void mostrarDetalhes() {
        System.out.println("Titular: " + titular + ", Saldo: R$" + saldo);
    }

    public static void main(String[] args) {
        
        ContaCorrente conta = new ContaCorrente("Maria", 500.00);

        conta.mostrarDetalhes();

        conta.depositar(150);
        conta.sacar(100);
        conta.sacar(600); 
        conta.mostrarDetalhes();
    }
}
