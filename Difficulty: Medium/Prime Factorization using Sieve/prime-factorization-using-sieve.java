//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            Solution obj = new Solution();
            obj.sieve();
            List<Integer> ans = obj.findPrimeFactors(n);
            for (int e : ans) {
                System.out.print(e + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    public static int []spf;
    static void sieve() {
        int limit= (int) Math.pow(10,5);
        limit=2*(limit);
        spf=new int[limit+1];
        for(int i=0;i<=limit;i++){
            spf[i]=i;
        }
        for(int i=2;i*i<=limit;i++){
            if(spf[i]==i){
                for(int j=i*i;j<=limit;j=j+i){
                    spf[j]=i;
                }
            }
        }
    }

    static List<Integer> findPrimeFactors(int N) {
        List<Integer> ans=new ArrayList<>();
        if(N<2){
            return ans;
        }
        while(true){
            if(N==spf[N]){
                ans.add(spf[N]);
                break;
            }
            ans.add(spf[N]);
            N=N/spf[N];
        }
        Collections.sort(ans);
        return ans;
    }
}
