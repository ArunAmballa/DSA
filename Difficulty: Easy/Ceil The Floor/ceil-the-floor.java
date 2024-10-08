//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int x = Integer.parseInt(br.readLine());
            String[] input = br.readLine().split(" ");
            int[] arr = new int[input.length];
            for (int i = 0; i < input.length; i++) {
                arr[i] = Integer.parseInt(input[i]);
            }

            Solution ob = new Solution();
            int[] ans = ob.getFloorAndCeil(x, arr);
            System.out.println(ans[0] + " " + ans[1]);
        }
    }
}

// } Driver Code Ends




// User function Template for Java

class Solution {
    public int floor(int x, int []arr){
        int low=0;
        int high=arr.length-1;
        int ans=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]<=x){
                ans=arr[mid];
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        
        return ans;
        
    }
    public int ceil(int x,int []arr){
        int low=0;
        int high=arr.length-1;
        int ans=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]>=x){
                ans=arr[mid];
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        
        return ans;
        
    }
    public int[] getFloorAndCeil(int x, int[] arr) {
        Arrays.sort(arr);
        int []ans=new int[2];
        ans[0]=floor(x,arr);
        ans[1]=ceil(x,arr);
        return ans;
    }
}
