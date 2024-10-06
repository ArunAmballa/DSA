//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t;
        t = sc.nextInt();
        while (t-- > 0) {

            int n;
            n = sc.nextInt();

            int k;
            k = sc.nextInt();

            int[] v = new int[n];
            for (int i = 0; i < n; i++) v[i] = sc.nextInt();

            Solution obj = new Solution();
            int res = obj.solve(n, k, v);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    public static int findMin(int []stalls){
        int mini=Integer.MAX_VALUE;
        for(int i=0;i<stalls.length;i++){
            mini=Math.min(mini,stalls[i]);
        }
        return mini;
    }
    
    public static int findMax(int []stalls){
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<stalls.length;i++){
            maxi=Math.max(maxi,stalls[i]);
        }
        return maxi;
    }
    public static int helper(int []stalls,int minDistance){
        int lastCowIndex=0;
        int numberOfCows=1;
        for(int i=1;i<stalls.length;i++){
            if(stalls[i]-stalls[lastCowIndex]>=minDistance){
                lastCowIndex=i;
                numberOfCows=numberOfCows+1;
            }
        }
        return numberOfCows;
    }
    public static int solve(int n, int k, int[] stalls) {
        Arrays.sort(stalls);
        int low=1;
        int high=findMax(stalls)-findMin(stalls);
        int ans=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            int cowsPlaced=helper(stalls,mid);
            if(cowsPlaced>=k){
                ans=mid;
                low=mid+1;
            }else{
                high=mid-1;
            }
            
        }
        return ans;
    }
}