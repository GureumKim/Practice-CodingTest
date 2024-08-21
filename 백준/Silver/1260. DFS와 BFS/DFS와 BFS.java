import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private static List<Integer>[] adjList;
	private static boolean[] visited;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n, m, v;
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList[n + 1];
		for (int i = 1; i <= n; i++) {
			adjList[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			int s, e;
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			adjList[s].add(e);
			adjList[e].add(s);
		}
		
		for (int i = 1; i <= n; i++) {
			Collections.sort(adjList[i]);
		}
		
		visited = new boolean[n + 1];
		dfs(v);
		System.out.println();
		
		visited = new boolean[n + 1];
		bfs(v);
		
		
		br.close();
	}
	private static void dfs(int node) {
		visited[node] = true;
		System.out.print(node + " ");
		for (int neighbor : adjList[node]) {
			if (!visited[neighbor]) 
				dfs(neighbor);
		}
		
	}
	
private static void bfs(int startNode) {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(startNode);
		visited[startNode] = true;
		
		while(!queue.isEmpty()) {
			int node = queue.poll();
			System.out.print(node + " ");
			for (int neighbor : adjList[node]) {
				if (!visited[neighbor]) {
					queue.add(neighbor);
					visited[neighbor] = true;
				}
			}
		}
	}
}