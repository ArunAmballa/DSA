//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while (t-- > 0) {
            String inputLine[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int m = Integer.parseInt(inputLine[1]);
            long arr1[] = new long[n];
            long arr2[] = new long[m];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr1[i] = Long.parseLong(inputLine[i]);
            }
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < m; i++) {
                arr2[i] = Long.parseLong(inputLine[i]);
            }
            Solution ob = new Solution();
            ob.merge(n, m, arr1, arr2);

            StringBuffer str = new StringBuffer();
            for (int i = 0; i < n; i++) {
                str.append(arr1[i] + " ");
            }
            for (int i = 0; i < m; i++) {
                str.append(arr2[i] + " ");
            }
            System.out.println(str);
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    // Function to merge the arrays.
    public static void merge(int n, int m, long arr1[], long arr2[]) {
        int left=n-1;
        int right=0;
        while(left>=0 && right<m){
            if(arr1[left]>arr2[right]){
                long temp=arr1[left];
                arr1[left]=arr2[right];
                arr2[right]=temp;
                left=left-1;
                right=right+1;
            }else{
                break;
            }
        }
        Arrays.sort(arr1);
        Arrays.sort(arr2);
    }
}
