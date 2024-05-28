import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] chess = {1, 1, 2, 2, 2, 8};
        String[] input = br.readLine().split(" ");

        for (int i=0; i<6; i++){
            int inp = Integer.parseInt(input[i]);
            if (chess[i] == inp){
                bw.write("0 ");
            }
            else {
                bw.write("" + (chess[i] - inp) + " ");
            }
        }
        br.close();
        bw.close();
    }
}