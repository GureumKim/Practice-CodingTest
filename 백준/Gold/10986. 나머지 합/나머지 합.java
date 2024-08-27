import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		long[] accSum = new long[N + 1];
		// 얘도 long 타입이어야 되는게 nC2 했을 때 범위 초과 할 수 있다.
		long[] remainderCount = new long[M];
		// 이 부분!!!
		long ans = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			accSum[i] = Integer.parseInt(st.nextToken()) + accSum[i - 1];
			int remainder = (int) (accSum[i] % M);
			if (remainder == 0) {
				ans++;
			}
			remainderCount[remainder]++;
		}
		
		for (int i = 0; i < M; i++) {
			if (remainderCount[i] > 1) {
				ans += remainderCount[i] * (remainderCount[i] - 1) / 2;
			}		
		}
		System.out.println(ans);
	}
}