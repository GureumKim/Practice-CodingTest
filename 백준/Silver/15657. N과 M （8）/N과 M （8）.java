import java.io.*;
import java.util.*;


public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		
		
		int N, M;
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer> num = new ArrayList<>();
		ArrayList<Integer> sequence = new ArrayList<>(M);
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			num.add(Integer.parseInt(st.nextToken()));
		}
		// sort 참고. https://hianna.tistory.com/569
		Collections.sort(num);
		
		dfs(N, M, num, sequence, 0, 0);
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	private static void dfs(int n, int m, ArrayList<Integer> num, ArrayList<Integer> sequence, int start, int level) throws IOException {
		if (level == m) {
			for (int i = 0; i < m; i++) {
				bw.write(sequence.get(i) + " ");
			}
			bw.write("\n");
			return;
		}
		
		for (int i = start; i < n; i++) {
			sequence.add(level, num.get(i));
			dfs(n, m, num, sequence, i, level+1);
		}
	}
}
