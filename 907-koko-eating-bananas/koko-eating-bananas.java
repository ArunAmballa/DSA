class Solution {

    public boolean helper(int []piles, int mid, int h){
        long countHours=0;
        int length=piles.length;
        for(int i=0;i<length;i++){
            countHours = countHours + (int) Math.ceil((double) piles[i]/ (double) mid);
        }
        if(countHours<=h){
            return true;
        }
        return false;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int low=1;
        int high=Arrays.stream(piles).max().getAsInt();
        int ans=-1;
        while(low<=high){
            int mid=(low+high)/2;
            boolean flag=helper(piles,mid,h);
            if(flag==true){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
    }
}