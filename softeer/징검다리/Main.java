/**
 * 링크. https://softeer.ai/practice/6293
 * LIS를 활용한 DP 문제
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] h = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			h[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[N];
		int max_length = 0;
		for (int i=0; i < N; i++) {
			dp[i] = 1;
			for (int j =0; j < i; j++) {
				if (h[i] > h[j]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
				}
			}
			max_length = Math.max(max_length, dp[i]);
		}
		
		System.out.println(max_length);
		br.close();
	}

}