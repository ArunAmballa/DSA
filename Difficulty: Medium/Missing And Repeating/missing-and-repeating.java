//{ Driver Code Starts
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String input = br.readLine();
            String[] inputs = input.split(" ");
            int[] arr = new int[inputs.length];

            for (int i = 0; i < inputs.length; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            int[] ans = new Solve().findTwoElement(arr);
            System.out.println(ans[0] + " " + ans[1]);
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solve {
    int[] findTwoElement(int arr[]) {
        int length=arr.length;
        int xor=0;
        for(int i=0;i<length;i++){
            xor=xor^arr[i];
            xor=xor^(i+1);
        }
        int setBit=-1;
        for(int i=0;i<32;i++){
            if((xor&(1<<i))!=0){
                setBit=i;
                break;
            }
        }
        int zero=0;
        int one=0;
        for(int i=0;i<length;i++){
            if((arr[i]&(1<<setBit))!=0){
                one=one^arr[i];
            }else{
                zero=zero^arr[i];
            }
        }
        
        for(int i=1;i<=length;i++){
            if((i&(1<<setBit))!=0){
             one=one^i;
            }else{
                zero=zero^i;
            }
        }
        int count=0;
        for(int i=0;i<length;i++){
            if(arr[i]==zero){
              count++;  
            }
        }
        if(count==2){
            return new int[]{zero,one};
        }
        
        return new int[]{one,zero};
    }
}
