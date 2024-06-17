import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i < n; i++) {
			for (int j = n-1-i; j >0 ; j-- ) {
				System.out.print(" ");
			}
			for (int j = n-1-i; j<n; j++) {
				System.out.print('*');
			}
			System.out.print("\n");
		}
		br.close();
	}
}