/** 문제 조건에서 조심할 점!
 * StringTokenizer를 사용하지 않을 경우 만약 입력받은 문자가 공백일 경우를 생각해야 함.
*/
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String in = sc.nextLine();
		sc.close();
		
		StringTokenizer st = new StringTokenizer(in, " ");
		
		System.out.println(st.countTokens());
	}
}