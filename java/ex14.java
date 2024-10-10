public class ex14 {
    static class Configuracao {
        private static Configuracao instancia;
    
        private Configuracao() {}
    
        public static Configuracao getInstancia() {
            if (instancia == null) {
                instancia = new Configuracao();
            }
            return instancia;
        }
    }
    
}
