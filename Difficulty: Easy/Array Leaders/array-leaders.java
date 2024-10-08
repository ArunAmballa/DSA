//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Array {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter ot = new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim()); // Inputting the testcases

        while (t-- > 0) {

            // input size of array
            int n = Integer.parseInt(br.readLine().trim());
            int arr[] = new int[n];
            String inputLine[] = br.readLine().trim().split(" ");

            // inserting elements in the array
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            Solution obj = new Solution();

            StringBuffer str = new StringBuffer();
            ArrayList<Integer> res = new ArrayList<Integer>();

            // calling leaders() function
            res = obj.leaders(n, arr);

            for (int i = 0; i < res.size(); i++) {
                ot.print(res.get(i) + " ");
            }

            ot.println();
        }
        ot.close();
    }
}

// } Driver Code Ends


class Solution {
    // Function to find the leaders in the array.
    static void reverse(ArrayList<Integer> ans){
        int low=0;
        int high=ans.size()-1;
        while(low<high){
            int temp=ans.get(low);
            ans.set(low,ans.get(high));
            ans.set(high,temp);
            low=low+1;
            high=high-1;
        }
    }
    static ArrayList<Integer> leaders(int n, int arr[]) {
        
        ArrayList<Integer> ans=new ArrayList<>();
        int length=arr.length;
        int maximum=arr[length-1];
        ans.add(arr[length-1]);
        if(length==0){
            return ans;
        }
        
        for(int i=length-2;i>=0;i--){
            if(arr[i]>=maximum){
                ans.add(arr[i]);
                maximum=Math.max(maximum,arr[i]);
            }
        }
        reverse(ans);
        return ans;
    
        
    }
}
