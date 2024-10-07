//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int arr[][] = new int[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            int ans = new Solution().rowWithMax1s(arr);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    public int ceil(int []nums){
        int low=0;
        int high=nums.length-1;
        int index=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]==1){
                index=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return index;
    }
    public int rowWithMax1s(int arr[][]) {
        int maxi=0;
        int answerIndex=-1;
        int rows=arr.length;
        int columns=arr[0].length;
        for(int i=0;i<rows;i++){
            int index=ceil(arr[i]);
            if(index!=-1){
                if(columns-index > maxi){
                    maxi=columns-index;
                    answerIndex=i;
                }
            }
            
        }
        return answerIndex;
    }
}