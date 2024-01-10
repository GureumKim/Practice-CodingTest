//import java.util.Scanner;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
//    public static void main(String[] args) {
//
//        Scanner sc = new Scanner(System.in);
//
//        int N = sc.nextInt();
//        int[] arr = new int[N];
//
//        for (int i=0;i<N;i++){
//            arr[i] = sc.nextInt();
//        }
//
//        Arrays.sort(arr);
//
//        int M = sc.nextInt();
//
//        StringBuilder sb = new StringBuilder();
//        for(int i = 0; i < M; i++){
//            if (binarySearch(arr, sc.nextInt()) >= 0){
//                sb.append(1).append('\n');
//            }
//            else{
//                sb.append(0).append('\n');
//            }
//        }
//        System.out.println(sb);
//    }
    public static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++){
//            Arrays안에 binarySearch란 내장 함수 있나 봄
//            Arrays.binarySearch(arr, Integer.parseInt(st.nextToken())) 사용해도 됨
            if (binarySearch(Integer.parseInt(st.nextToken()))>=0){
                sb.append(1).append('\n');
            }
            else {
                sb.append(0).append('\n');
            }
        }
        System.out.println(sb);
    }
//    /**
//     * scanner 버전
//     * @param arr 정렬된 배열
//     * @param key 찾으려는 값
//     * @return key와 일치하는 배열의 인덱스
//     */
//
//    public static int binarySearch(int[] arr, int key){
//        int lo = 0;
//        int hi = arr.length - 1;
//
//        while(lo <= hi){
//
//            int mid = (lo+hi) / 2;
//            if (key < arr[mid])
//                    hi = mid - 1;
//            else if(key > arr[mid]){
//                lo = mid + 1;
//            }
//            else {
//                return mid;
//            }
//        }
//        return -1;
//    }
    /**
     * @param key 찾으려는 값
     * @return key와 일치하는 배열의 인덱스
     */
    public static int binarySearch(int key){
        int lo = 0;
        int hi = arr.length - 1;

        while(lo <=hi){
            int mid = (lo+hi)/2;
            if(key < arr[mid])
                hi = mid - 1;
            else if(key > arr[mid])
                lo = mid + 1;
            else
                return mid;
        }

        return -1;
    }
}
