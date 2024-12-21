import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] res = new int[26];
		Arrays.fill(res, -1);
		char[] word = br.readLine().toCharArray();
		
		for (int i = 0; i < word.length; i++) {
			if (res[word[i] - 'a'] == -1)
				res[word[i] - 'a'] = i;
		}
		br.close();
		
		
		String result = ""; 
		for (int i = 0; i < 25; i++) {
			result += res[i] + " ";
		}
		result += res[25];
		System.out.println(result);
	}
}
