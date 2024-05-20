import java.io.*;

public class Main {
   public static void main(String[] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

       BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

       String[] input = br.readLine().split(" ");
       int n, m;
       n = Integer.parseInt(input[0]);
       m = Integer.parseInt(input[1]);

       if(n > m) {
           bw.write(">");
       } else if (n < m) {
           bw.write("<");
       } else {
           bw.write("==");
       }
       bw.close();
    }
}