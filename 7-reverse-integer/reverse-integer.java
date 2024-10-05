class Solution {
    public int reverse(int x) {
        int y=Math.abs(x);
        long ans=0;

        while(y!=0){
            int lastElement=y%10;
            ans=ans*10+lastElement;
            y=y/10;
        }

        if(ans<Integer.MIN_VALUE || ans>Integer.MAX_VALUE){
            return 0;
        }
        int finalAnswer=(int) ans;
        if(x<0){
            return -finalAnswer;
        }
        return finalAnswer;
        
    }
}