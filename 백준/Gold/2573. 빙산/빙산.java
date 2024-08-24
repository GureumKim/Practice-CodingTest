import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		
		// field 2차원 배열 생성
		int[][] field = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				field[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 빙하의 위치와 높이 데이터
		Queue<int[]> glacier = new LinkedList<>();
		for (int i = 1; i <= N - 1; i++) {
			for (int j = 1; j <= M - 1; j++) {
				if (field[i][j] != 0)
					glacier.add(new int[]{i, j, field[i][j]});
			}
		}
		
		br.close();
		
		int years = 0;
		while (!glacier.isEmpty()) {
			years++;
			glacier = melt(field, glacier, N, M);
			int groupCount = 0;
			boolean[][] visited = new boolean[N][M];
			
			for (int i = 0; i < N-1; i++) {
				for (int j = 0; j < M-1; j++) {
					if (field[i][j] != 0 && !visited[i][j]) {
						grouping(field, visited, i, j, N, M);
						groupCount += 1;
					}
					if (groupCount > 1) {
						System.out.println(years);
						return;
					}
				}
			}
		}
		System.out.println(0);
	}
	
	private static Queue<int[]> melt(int[][] field, Queue<int[]> queue, int n, int m) {
		Queue<int[]> nextGlacier = new LinkedList<>();
		List<int[]> melted = new ArrayList<>();
		int[] dx = new int[] {0, 0, -1, 1};
		int[] dy = new int[] {-1, 1, 0, 0};
		while (!queue.isEmpty()) {
			int[] data = queue.poll();
			int y = data[0];
			int x = data[1];
			int h = data[2];
			
			int cnt = 0;
			for (int k = 0; k < 4; k++) {
				int ny, nx;
				ny = dy[k] + y;
				nx = dx[k] + x;
				if (ny < 0 || nx < 0 || ny > n || nx > m) continue;
				if (field[ny][nx] == 0) {
					cnt += 1;
				}
			}
			if (h - cnt > 0) {
				nextGlacier.add(new int[]{y, x, h - cnt});
				field[y][x] = h - cnt;
			}
			else 
				melted.add(new int[] {y, x});
		}
		for (int i = 0; i < melted.size(); i++) {
			int[] data = melted.get(i);
			int y = data[0];
			int x = data[1];
			field[y][x] = 0;
		}
		
		return nextGlacier;
	}
	
	private static void grouping(int[][] field, boolean[][] visited, int sY, int sX, int n, int m) {
		int[] dy = {1, -1, 0, 0};
		int[] dx = {0, 0, 1, -1};
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {sY, sX});
		visited[sY][sX] = true;
		
		while (!queue.isEmpty()) {
			int[] data = queue.poll();
			int y = data[0];
			int x = data[1];
			for (int i = 0; i < 4; i++) {
				int ny = dy[i] + y;
				int nx = dx[i] + x;
				if (ny < 1 || nx < 1 || ny >= n-1 || nx >= m-1 || visited[ny][nx] || field[ny][nx] == 0) continue;
				
				visited[ny][nx] = true;
				queue.add(new int[] {ny, nx});
				
			}
		}
	}
}
