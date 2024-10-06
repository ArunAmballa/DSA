//{ Driver Code Starts
// Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int a[] = new int[n];

            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            int m = sc.nextInt();
            Solution ob = new Solution();
            System.out.println(ob.findPages(n, a, m));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    
    public static int findMax(int []arr){
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<arr.length;i++){
            maxi=Math.max(maxi,arr[i]);
        }
        
        return maxi;
    }
    
    
    public static long findSum(int []arr){
        long sum=0;
        for(int i=0;i<arr.length;i++){
            sum=sum+arr[i];
        }
        return sum;
    }
    
    public static long helper(int []arr,long maximumPages){
        long students=0;
        long currentPages=0;
        for(int i=0;i<arr.length;i++){
            currentPages=currentPages+arr[i];
            if(currentPages>maximumPages){
                students+=1;
                currentPages=arr[i];
            }
        }
        return students+1;
        
    }
    public static long findPages(int n, int[] arr, int m) {
        int length=arr.length;
        if(m>length){
            return -1;
        }
        long low=findMax(arr);
        long high=findSum(arr);
        long ans=-1;
        while(low<=high){
            long mid=low+(high-low)/2;
            long numberOfStudents=helper(arr,mid);
            if(numberOfStudents<=m){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        
        return ans;
        
    }
};