class Solution {
    public int countDigits(int n){
        int count=0;
        while(n!=0){
            count=count+1;
            n=n/10;
        
        }

        return count;

    }
    public boolean isArmstrong(int n) {

        int ans=0;
        int copy=n;
        int digits=countDigits(n);
        while(copy!=0){
            int lastElement=copy%10;
            ans=ans+(int)Math.pow(lastElement,digits);
            copy=copy/10;
        }

        return (ans==n) ? true : false;
        
    }
}