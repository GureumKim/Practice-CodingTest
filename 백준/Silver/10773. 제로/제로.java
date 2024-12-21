import java.io.BufferedReader;
//import java.io.FileReader;
import java.io.IOException;
import java.util.Stack;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < k; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0)
				stack.pop();
			else
				stack.add(num);
		}
		int ans = 0;
		while (stack.isEmpty() == false) {
			ans += stack.pop();
		}
		System.out.println(ans);
		br.close();
	}
}
