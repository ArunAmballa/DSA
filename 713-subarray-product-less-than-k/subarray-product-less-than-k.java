class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int left=0;
        int right=0;
        int length=nums.length;
        int count=0;
        int product=1;
        while(right<length){
            product=product*nums[right];
            while(product>=k && left<right){
                product=(product/nums[left]);
                left=left+1;
            }
            if(product<k){
                count=count+(right-left+1);
            }
            right++;
        } 
        return count;
    }
}