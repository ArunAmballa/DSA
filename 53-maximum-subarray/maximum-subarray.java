class Solution {
    public int maxSubArray(int[] nums) {

        int maximumSum=Integer.MIN_VALUE;
        int prefixSum=0;
        for(int i=0;i<nums.length;i++){
            prefixSum=prefixSum+nums[i];
            maximumSum=Math.max(maximumSum,prefixSum);
            if(prefixSum<0){
                prefixSum=0;
            }
        }      

        return maximumSum;  
    }
}