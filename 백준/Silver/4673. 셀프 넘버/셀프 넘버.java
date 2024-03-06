import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        boolean[] sieve= new boolean[10001]; // 기본 false로 초기화 -> 0
        for (int i=1; i<10001; i++){
            if (sieve[i]) continue;
            int next = i;
            while (true) {
                // now와 mod를 int 형으로 초기화하는데
//                now는 next의 값을 mod는 선언만
                int now = next, mod;
                while (true) {
                    mod = now %10;
                    now /= 10;
                    next += mod;
                    if (now == 0) break;
                }
                if (next > 10000) break;
                sieve[next] = true;
            }
        }
        for (int i = 1; i< 10001; i++){
            if (!sieve[i]) {
                bw.write(i+"\n");
            }
        }

        bw.close();
    }

}
