import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//	N, M, 대상 배열 입력 받기 
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] num = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			num[i] = sc.nextInt();
		}
		
		// 구간 합 배열 생성
		int[] accSum = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			accSum[i] = num[i] + accSum[i - 1];
		}
		
		// 구간 합 구하기
		
		for (int i = 0; i < M; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(accSum[end] - accSum[start-1]);
		}
	}
}
