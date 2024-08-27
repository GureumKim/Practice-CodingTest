import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] num = new int[n + 1][n + 1];
		int[][] accSum = new int[n + 1][n + 1];
		
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				accSum[i][j] = Integer.parseInt(st.nextToken()) + accSum[i][j - 1] + accSum[i - 1][j] - accSum[i - 1][j - 1];
			}
		}
		
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			int ans = accSum[x2][y2] - accSum[x1 - 1][y2] - accSum[x2][y1 - 1] + accSum[x1 - 1][y1 - 1];
			System.out.println(ans);
		}
	}
}
