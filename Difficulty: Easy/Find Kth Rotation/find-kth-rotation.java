//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    // Driver code
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            List<Integer> arr = new ArrayList<>();
            String input1 = sc.nextLine();
            Scanner ss1 = new Scanner(input1);
            while (ss1.hasNextInt()) {
                arr.add(ss1.nextInt());
            }
            Solution ob = new Solution();
            int res = ob.findKRotation(arr);
            System.out.println(res);
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    public int findKRotation(List<Integer> nums) {
        int minimum=Integer.MAX_VALUE;
        int minIndex=-1;
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums.get(low)<=nums.get(mid)){
                if(nums.get(low)<minimum){
                    minimum=nums.get(low);
                    minIndex=low;
                }
                low=mid+1;
            }else if(nums.get(mid)<=nums.get(high)){
                if(nums.get(mid)<minimum){
                    minimum=nums.get(mid);
                    minIndex=mid;
                }
                high=mid-1;
            }
        }
        return minIndex;
        
    }
}