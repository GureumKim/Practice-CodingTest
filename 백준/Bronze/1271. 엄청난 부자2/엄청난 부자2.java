import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String[] input = br.readLine().split(" ");
        BigInteger n = new BigInteger(input[0]);
        BigInteger m = new BigInteger(input[1]);

        BigInteger expo = n.divide(m);
        BigInteger rest = n.remainder(m);

        bw.write(expo.toString());
        bw.newLine();
        bw.write(rest.toString());

//        bw.flush();
        bw.close();

    }
}