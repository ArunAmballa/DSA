//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class Sorting {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            long arr[] = new long[str.length];
            for (int i = 0; i < str.length; i++) arr[i] = Integer.parseInt(str[i]);
            System.out.println(new Solution().inversionCount(arr));
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    
    
    static int merge(long []arr,int low,int mid,int high){
        int i=low;
        int j=mid+1;
        ArrayList<Long> temp=new ArrayList<>();
        int cnt=0;
        while(i<=mid && j<=high){
            if(arr[i]<=arr[j]){
                temp.add(arr[i]);
                i=i+1;
            }else{
                temp.add(arr[j]);
                cnt=cnt+(mid-i+1);
                j=j+1;
            }
        }
        
        while(i<=mid){
            temp.add(arr[i]);
            i=i+1;
        }
        while(j<=high){
            temp.add(arr[j]);
            j=j+1;
        }
        
        for(int k=low;k<=high;k++){
            arr[k]=temp.get(k-low);
        }
        return cnt;
    }
    
    static int mergeSort(long []arr,int low, int high){
        int cnt=0;
        if(low>=high){
            return cnt;
        }
        int mid=(low+high)/2;
        cnt+=mergeSort(arr,low,mid);
        cnt+=mergeSort(arr,mid+1,high);
        cnt+=merge(arr,low,mid,high);
        return cnt;
    }
    static long inversionCount(long arr[]) {
        int low=0;
        int high=arr.length-1;
        return mergeSort(arr,0,high);
        
    }
}