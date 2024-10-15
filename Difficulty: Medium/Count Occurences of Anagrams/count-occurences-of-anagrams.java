//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    // Driver code
    public static void main(String[] args) throws Exception {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            String txt = br.readLine().trim();
            String pat = br.readLine().trim();

            int ans = new Solution().search(pat, txt);

            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {

    int search(String pat, String txt) {
        int []p=new int[26];
        int []t=new int[26];
        int count=0;
        for(int i=0;i<pat.length();i++){
            p[pat.charAt(i)-'a']=p[pat.charAt(i)-'a']+1;
        }
        int k=pat.length();
        for(int i=0;i<k;i++){
            t[txt.charAt(i)-'a']=t[txt.charAt(i)-'a']+1;
        }
        boolean flag=true;
        for(int i=0;i<26;i++){
            if(p[i]!=t[i]){
                flag=false;
                break;
            }
        }
        if(flag==true) count=count+1;
        for(int i=k;i<txt.length();i++){
            t[txt.charAt(i-k)-'a']=t[txt.charAt(i-k)-'a']-1;
            t[txt.charAt(i)-'a']=t[txt.charAt(i)-'a']+1;
            boolean Tflag=true;
            for(int j=0;j<26;j++){
                if(p[j]!=t[j]){
                    Tflag=false;
                    break;
                }
            }
            if(Tflag==true) count=count+1;
        }
        return count;
    }
}