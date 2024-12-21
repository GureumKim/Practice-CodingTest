import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		
		int answer = 0;
		int n = Integer.parseInt(br.readLine());
		String num = br.readLine();
		for (int i = 0; i < n ; i++) {
			answer += num.charAt(i) - '0';
		}
		
		System.out.println(answer);
		br.close();
	}
}
