import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		//	N, M, 대상 배열 입력 받기 
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		
		st = new StringTokenizer(br.readLine());
		// 구간 합 배열 생성
		int[] accSum = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			accSum[i] = accSum[i - 1] + Integer.parseInt(st.nextToken());
		}
		
		// 구간 합 구하
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int fromIdx = Integer.parseInt(st.nextToken());
			int toIdx = Integer.parseInt(st.nextToken());
			System.out.println(accSum[toIdx] - accSum[fromIdx - 1]);
		}
	}
}
