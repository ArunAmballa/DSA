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
            String input_line1[] = read.readLine().trim().split("\\s+");
            int k = Integer.parseInt(input_line1[0]);
            int n = Integer.parseInt(input_line1[1]);
            String input_line[] = read.readLine().trim().split("\\s+");
            int arr[]= new int[n];
            for(int i = 0; i < n; i++)
                arr[i] = Integer.parseInt(input_line[i]);
            
            Solution ob = new Solution();
            System.out.println(ob.minTime(arr,n,k));
        }
    }
}


// } Driver Code Ends


//User function Template for Java

 class Solution{
     
     public static int findMax(int []nums){
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            maxi=Math.max(maxi,nums[i]);
        }
        return maxi;
    }
    public static long findSum(int []nums){
        long sum=0;
        for(int i=0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        return sum;
    }
    public static int helper(int []nums,long maximumSubArraySum){
        long subArraySum=0;
        int numberOfSubarray=0;
        for(int i=0;i<nums.length;i++){
            subArraySum=subArraySum+nums[i];
            if(subArraySum>maximumSubArraySum){
                numberOfSubarray+=1;
                subArraySum=nums[i];
            }
        }
        return numberOfSubarray+1;
    }
    static long minTime(int[] nums,int n,int k){
        long low=findMax(nums);
        long high=findSum(nums);
        while(low<=high){
            long mid=low+(high-low)/2;
            int numberOfSubArrays=helper(nums,mid);
            if(numberOfSubArrays<=k){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return low;
    }
}


