import java.io.*;

public class Main {
	static int recursionCnt = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		String[] testCase = new String[n];
		for (int i = 0; i < n; i++) {
			testCase[i] = br.readLine();
		}
		
//		String[] answer = new String[n];
//		String answer = ""; // Bad case -> String은 불변 객체이므로 answer +=를 반복할 경우 새로운 문자열 객체가 계속 생성되어 성능 저하 위험 => StringButiler 사용
		StringBuilder answer = new StringBuilder();
		for (int i = 0; i < n; i++) {
			recursionCnt = 0;
			int res = isPalindrome(testCase[i]);
//			answer[i] = "" + res + recursionCnt;
			answer.append(res).append(" ").append(recursionCnt).append("\n");
		}
		
		bw.write(answer.toString());
		br.close();
		bw.close();
	}

	private static int recursion(String s, int l, int r) {
		recursionCnt++;
		
		if (l >= r)
			return 1;
		else if (s.charAt(l) != s.charAt(r)) {
			return 0;
		}
		else
			return recursion(s, l + 1, r - 1);
	}
	
	private static int isPalindrome(String s) {
		return recursion(s, 0, s.length() - 1);
	}

}
