import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new FileReader("./input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		Set<Integer> remainder = new HashSet<Integer>();
		for (int i = 0; i < 10; i++) {
			remainder.add(Integer.parseInt(br.readLine()) % 42);
		}
		
		System.out.println(remainder.size());
		br.close();
	}
}
