import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N, M;
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		int[][] field = new int[N][M];
		// 컬렉션 어떻게 써야하는지 구조 알아보자 
		Queue<int[]> queue = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
				if (field[i][j] != 0) {
					queue.add(new int[] {i, j ,field[i][j]});
				}
			}
		}
		
		int year = 0;
		while (!queue.isEmpty()) {
			queue = melting(field, queue);
			year++;
			int group = 0;
			boolean[][] visited = new boolean[N][M];
			for (int i = 1; i < N - 1; i++) {
				for (int j = 1; j < M - 1; j++) {
					if (field[i][j] != 0 && !visited[i][j]) {
						grouping(field, visited, N, M, i, j);
						group++;
					}
					if (group > 1) {
						System.out.println(year);
						return;
					}
				}
			}
		}
		System.out.println(0);
	}
	
	// 왜 여기다 static 써야 되지?
	private static Queue<int[]> melting(int[][] field, Queue<int[]> glacier) {
		int[] dx = {1, -1, 0, 0};
		int[] dy = {0, 0, 1, -1};
		Queue<int[]> restGlacier = new LinkedList<>();
		List<int[]> melted = new ArrayList<>();
		
		while (!glacier.isEmpty()) {
			int[] data = glacier.poll();
			int y = data[0];
			int x = data[1];
			int h = data[2];
			
			int cnt = 0;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (field[ny][nx] == 0) cnt++;
			}
			if (h - cnt > 0) {
				restGlacier.add(new int[] {y, x, h - cnt});
				field[y][x] = h - cnt;
			} else {
				melted.add(new int[] {y, x});
			}
		}
		for (int i = 0; i < melted.size(); i++) {
			field[melted.get(i)[0]][melted.get(i)[1]] = 0;
		}
		
		
		return restGlacier;
	}
	
	private static void grouping(int[][] field, boolean[][] visited, int n, int m, int startY, int startX) {
		int[] dx = {1, -1, 0, 0};
		int[] dy = {0, 0, 1, -1};
	
		Stack<int[]> stack = new Stack<>();
		stack.add(new int[]{startX, startY});
		visited[startY][startX] = true;
		while (!stack.isEmpty()) {
			int[] data = stack.pop();
			int x = data[0];
			int y = data[1];
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				
				if(nx < 1 || ny < 1 || nx >= m - 1 || ny >= n - 1 || field[ny][nx] == 0 || visited[ny][nx]) continue;
				stack.add(new int[] {nx, ny});
				visited[ny][nx] = true;
			}
		}
	}
}