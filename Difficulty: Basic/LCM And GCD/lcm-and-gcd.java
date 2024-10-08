//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            Long A = Long.parseLong(S[0]);
            Long B = Long.parseLong(S[1]);

            Solution ob = new Solution();
            Long[] ptr = ob.lcmAndGcd(A,B);
            
            System.out.print(ptr[0]);
            System.out.print(" ");
            System.out.println(ptr[1]);
        }
    }
}
// } Driver Code Ends


class Solution {
    
    public static Long GCD(Long n1, Long n2){
        
        while(n1!=0 && n2!=0){
            if(n1>n2){
                n1=n1%n2;
            }else{
                n2=n2%n1;
            }
        }
        if(n1==0) return n2;
        return n1;
    }
    
    public static Long LCM(Long n1, Long n2, Long gcd){
        
        return (n1*n2)/gcd;
    }
    static Long[] lcmAndGcd(Long A , Long B) {
        Long []ans=new Long[2];
        Long gcd=GCD(A,B);
        ans[1]=gcd;
        ans[0]=LCM(A,B,gcd);
        
        return ans;
    }
};