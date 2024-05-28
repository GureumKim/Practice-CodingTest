import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t<T; t++) {
            String st = br.readLine();
            bw.write("" + st.charAt(0) + st.charAt(st.length()-1) + "\n");
        }
        br.close();
        bw.close();
    }
}