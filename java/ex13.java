public class ex13 {
    class Matematica {
        public static long fatorial(int n) {
            if (n == 0) return 1;
            return n * fatorial(n - 1);
        }
    }
}
