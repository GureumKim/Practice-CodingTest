import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int S, N, M, U;
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	U = S = Integer.parseInt(st.nextToken());
    	N = Integer.parseInt(st.nextToken());
    	M = Integer.parseInt(st.nextToken());
    	
    	int amt = 0;
    	
    	int[] arr = new int[S];
    	for (int i = 0; i < N+M; i++) {
    		String cmd = br.readLine();
    		if (cmd.equals("1")) {
    			if (amt == U) {
    				
    				int[] newArr = new int[2*U];
    				for (int j = 0; j < U; j++) {
    					newArr[j] = arr[j];
    				}
    				U *= 2;
    				arr = newArr;
    			}
				arr[amt] = i;
				
				amt += 1;
    		} else if(cmd.equals("0")) {

    			// 저장된 원소 없을 때는 주어지지 않는다고 함
    			arr[amt-1] = -1;
    			amt -= 1;
    		}
    	}
    	System.out.println(U);
    	br.close();
    }
}