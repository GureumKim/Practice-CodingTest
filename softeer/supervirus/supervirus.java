//import java.io.*;
//import java.util.*;
//
//
//public class Main {
//    public static final long MOD = 1000000007;
//
//    private static long f(long x, long y){
//        if (y == 1){
//            return x;
//        } else {
//            long a = f(x,y/2);
//            if (y%2==0)
//                return a*a%MOD;
//            else
//                return (a*a%MOD)*x%MOD;
//        }
//    }
//
//    public static void main(String[] args){
//        Scanner sc = new Scanner(System.in);
//        long k = sc.nextLong();
//        long p = sc.nextLong();
//        long n = sc.nextLong();
//
//        long result = k*f(p,n*10)%MOD;
//
//        System.out.println(result);
//    }
//}


import java.util.*;
import java.io.*;

public class Main{
    public static final long MOD = 1000000007;

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long k = Long.parseLong(st.nextToken());
        long p = Long.parseLong(st.nextToken());
        long n = Long.parseLong(st.nextToken());

        n *= 10;

        long result = recursion(p,n);
        System.out.println(k*result%MOD);
    }


    static long recursion(long p, long n){
        if (n==1)
            return p;

        long cur = recursion(p,n/2);
        if (n % 2 == 1)
            return (cur*cur%MOD)*p%MOD;
        else
            return cur*cur%MOD;
    }
}