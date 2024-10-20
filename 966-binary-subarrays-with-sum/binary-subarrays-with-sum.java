class Solution {
    public int helper(int []nums,int k){
        if(k<0){
            return 0;
        }
        int length=nums.length;
        int left=0;
        int right=0;
        int count=0;
        int sum=0;
        while(right<length){
            sum+=nums[right];
            while(sum>k){
                sum-=nums[left];
                left=left+1;
            }
            count+=(right-left+1);
            right++;
        }
        return count;
    }
    public int numSubarraysWithSum(int[] nums, int goal) {
        return helper(nums,goal)-helper(nums,goal-1);
    }
}