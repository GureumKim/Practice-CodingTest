import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] res = new int[26];
		Arrays.fill(res, -1);
		String word = br.readLine();
		
		for (int i = word.length() - 1; i >= 0; i--) {
				res[word.charAt(i) - 'a'] = i;
		}
		
		br.close();
		
		String result = ""; 
		for (int i = 0; i < res.length; i++) {
			result += res[i] + " ";
		}
		System.out.println(result);
	}
}
