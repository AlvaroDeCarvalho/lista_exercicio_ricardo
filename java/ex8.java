import java.util.ArrayList;
import java.util.List;
public class ex8 {

class Empregado {
    private String nome;
    private String cargo;
    private double salario;

    public Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    // Getters e Setters
    public String getNome() { return nome; }
    public String getCargo() { return cargo; }
    public double getSalario() { return salario; }
}

class Empresa {
    private List<Empregado> empregados;

    public Empresa() {
        this.empregados = new ArrayList<>();
    }

    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    public List<Empregado> getEmpregados() {
        return empregados;
    }
}

}
