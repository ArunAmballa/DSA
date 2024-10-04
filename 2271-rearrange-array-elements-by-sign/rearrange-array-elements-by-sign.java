class Solution {
    public int[] rearrangeArray(int[] nums) {

        int length=nums.length;

        int []ans=new int[length];

        int posIndex=0;
        int negIndex=1;
        for(int i=0;i<length;i++){
            if(nums[i]>0){
                ans[posIndex]=nums[i];
                posIndex=posIndex+2;
            }else{
                ans[negIndex]=nums[i];
                negIndex=negIndex+2;
            }
        }

        return ans;
        
    }
}