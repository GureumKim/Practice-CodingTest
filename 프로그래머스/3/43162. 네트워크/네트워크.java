public class Solution {
	public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
        	if (visited[i]) continue;
        	
        	dfs(computers, n, visited, i);
        	answer++;
        }
        
        
        
        return answer;
    }
	
	private void dfs(int[][] computers, int n, boolean[] visited, int start) {
		visited[start] = true;
		
		for (int i = 0; i < n; i++) {
			if (computers[start][i] !=  0 && !visited[i]) dfs(computers, n, visited, i);
		}
	};
}
