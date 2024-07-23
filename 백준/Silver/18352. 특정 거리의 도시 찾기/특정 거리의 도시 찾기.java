import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        
        // 인접 리스트 생성
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            graph.get(s).add(new int[] {e, 1});
        }
        
        int[] distance = dijkstra(N, X, graph);
        
        boolean found = false;
        for (int i = 1; i <= N; i++) {
            if (distance[i] == K) {
                bw.write(i + "\n");
                found = true;
            }
        }
        
        if (!found) {
            bw.write("-1\n");
        }
        
        br.close();
        bw.flush();
        bw.close();
    }
    
    private static int[] dijkstra(int N, int start, List<List<int[]>> graph) {
        int[] distance = new int[N + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        
        distance[start] = 0;
        pq.add(new int[] {start, 0});
        
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int currentNode = current[0];
            int currentDist = current[1];
            
            if (currentDist > distance[currentNode]) continue;
            
            for (int[] neighbor : graph.get(currentNode)) {
                int nextNode = neighbor[0];
                int nextDist = currentDist + neighbor[1];
                
                if (nextDist < distance[nextNode]) {
                    distance[nextNode] = nextDist;
                    pq.add(new int[] { nextNode, nextDist });
                }
            }
        }
        return distance;
    }
}