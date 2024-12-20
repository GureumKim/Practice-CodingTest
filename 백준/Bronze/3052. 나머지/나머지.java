import java.io.*;
//import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		boolean[] remainder = new boolean[42];
		for (int i = 0; i < 10; i++) {
			remainder[Integer.parseInt(br.readLine()) % 42] = true; 
		}
		
		int cnt = 0;
		for (int i = 0; i < remainder.length; i++) {
			if (remainder[i] == true)
				cnt++;
		}
		
		br.close();
		System.out.println(cnt);
	}
}
