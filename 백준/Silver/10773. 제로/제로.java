import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		int[] stack =  new int[k];
		int top = -1;
		
		for (int i = 0; i < k; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0) {
				stack[top] = 0;
				top--;
			}
			else {
				top++;
				stack[top] = num;
			}
		}
		
		int ans = 0;
		for (int n : stack) {
			ans += n;
		}
		System.out.println(ans);
		br.close();
	}
}
