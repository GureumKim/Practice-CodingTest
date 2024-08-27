import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		double[] score = new double[n];
		
		double mx = Double.MIN_VALUE; 
		for (int i = 0; i < n; i++) {
			score[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			if (mx < score[i])
				mx = score[i];
		}
		double sum = 0;
		for (int i = 0; i < n; i++) {
			sum += score[i] / mx * 100;
		}
		double avg = sum / n;
		System.out.println(avg);
	}
}
