//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            int k = Integer.parseInt(br.readLine().trim());

            String[] line1 = br.readLine().trim().split(" ");
            int[] arr1 = new int[line1.length];
            for (int i = 0; i < line1.length; i++) {
                arr1[i] = Integer.parseInt(line1[i]);
            }

            String[] line2 = br.readLine().trim().split(" ");
            int[] arr2 = new int[line2.length];
            for (int i = 0; i < line2.length; i++) {
                arr2[i] = Integer.parseInt(line2[i]);
            }

            Solution ob = new Solution();
            System.out.println(ob.kthElement(k, arr1, arr2));
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    
    public long kthElement(int k, int nums1[], int nums2[]) {
        
        int n1=nums1.length;
        int n2=nums2.length;
        if(n1>n2){
            return kthElement(k,nums2,nums1);
        }
        int totalElements=n1+n2;
        int numberOfElementsInPartition=k;
        int low=Math.max(0,k-n2);
        int high=Math.min(k,n1);
        while(low<=high){
            int cut1=low+(high-low)/2;
            int cut2=numberOfElementsInPartition-cut1;
            int l1= (cut1-1>=0) ? nums1[cut1-1] : Integer.MIN_VALUE;
            int l2= (cut2-1>=0) ? nums2[cut2-1] : Integer.MIN_VALUE;
            int r1= (cut1<n1) ? nums1[cut1] : Integer.MAX_VALUE;
            int r2= (cut2<n2) ? nums2[cut2] : Integer.MAX_VALUE;
            if(l1<=r2 && l2<=r1){
                return Math.max(l1,l2);
            }else if (l1>r2){
                high=cut1-1;
            }else{
                low=cut1+1;
            }
        }

        return 0;
        
    }
}