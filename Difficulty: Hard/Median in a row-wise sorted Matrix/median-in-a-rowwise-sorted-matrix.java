//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;


class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            String S[] = read.readLine().split(" ");
            int R = Integer.parseInt(S[0]);
            int C = Integer.parseInt(S[1]);
            int matrix[][] = new int[R][C];
            int c = 0;
            for(int i = 0; i < R; i++){
                String line[]=read.readLine().trim().split(" ");
                for(int j = 0; j < C; j++){
                    matrix[i][j] = Integer.parseInt(line[j]);
                }
            }
            Solution ob = new Solution();
            int ans = ob.median(matrix, R, C);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    
    public int findMin(int [][]matrix,int rows){
        int mini=Integer.MAX_VALUE;
        for(int i=0;i<rows;i++){
            mini=Math.min(mini,matrix[i][0]);
        }
        return mini;
    }
    
    public int findMax(int [][]matrix,int rows,int columns){
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<rows;i++){
            maxi=Math.max(maxi,matrix[i][columns-1]);
        }
        return maxi;
        
    }
    
    public int upperBound(int []arr, int median){
        int low=0;
        int high=arr.length-1;
        int ans=arr.length;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]>median){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
        
    }
    
    public int helper(int [][]matrix, int median, int rows, int columns){
        int count=0;
        for(int i=0;i<rows;i++){
            count=count+upperBound(matrix[i],median);
        }
        return count;
        
    }
    
    int median(int matrix[][], int R, int C) {
        
        int low=findMin(matrix,R);
        int high=findMax(matrix,R,C);
        int ans=-1;
        int req=(R*C)/2;
        while(low<=high){
            int mid=low+(high-low)/2;
            int numberOfElements=helper(matrix,mid,R,C);
            if(numberOfElements>req){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
            
        }
        
        return ans;
        
    }
}