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
            int n = Integer.parseInt(br.readLine().trim());
            Solution ob = new Solution();
            int ans = ob.DivCountSum(n);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    public int numberOfDivisors(int n){
        int count=0;
        for(int i=1;i*i<=n;i++){
            if(n%i==0){
                if(i==n/i){
                    count++;
                }else{
                    count+=2;
                }
            }
        }
        return count;
    }
    public int DivCountSum(int n)
    {
        int finalCount=0;
        for(int i=1;i<=n;i++){
            finalCount+=numberOfDivisors(i);
        }
        return finalCount;
    }
}