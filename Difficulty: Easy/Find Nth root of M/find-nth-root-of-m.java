//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String s = br.readLine().trim();
            String[] S1 = s.split(" ");
            int n = Integer.parseInt(S1[0]);
            int m = Integer.parseInt(S1[1]);
            Solution ob = new Solution();
            int ans = ob.NthRoot(n, m);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    
    public int power(int x,int n,int m){
        long a=1;
        for(int i=0;i<n;i++){
            a=a*x;
            if(a>m){
                return 1;
            }
        }
        if(a==m){
                return 0;
            }
        return 2;
    }
    
    public int NthRoot(int n, int m){
        int low=1;
        int high=m;
        while(low<=high){
            int mid=low+(high-low)/2;
            int powerValue=power(mid,n,m);
            if(powerValue==0){
                return mid;
            }else if(powerValue==1){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return -1;
        
    }
}