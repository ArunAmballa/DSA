//{ Driver Code Starts


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
            int N = Integer.parseInt(br.readLine().trim());
            Solution ob = new Solution();
            int[] ans = ob.AllPrimeFactors(N);
            for(int i = 0; i < ans.length; i++)
                System.out.print(ans[i] + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends




class Solution
{
    public int[] AllPrimeFactors(int N)
    {
        ArrayList<Integer> ans=new ArrayList<>();
        
        for(int i=2;i<=N;i++){
            if(N%i==0){
                ans.add(i);
                while(N%i==0){
                    N=N/i;
                }
            }
        }
        int limit=ans.size();
        int []finalAnswer=new int[limit];
        for(int i=0;i<limit;i++){
            finalAnswer[i]=ans.get(i);
        }
        return finalAnswer;
    }
}