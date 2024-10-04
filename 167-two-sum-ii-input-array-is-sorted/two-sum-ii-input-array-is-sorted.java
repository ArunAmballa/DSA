class Solution {
    public int[] twoSum(int[] nums, int target) {
        int length=nums.length;
        int []ans=new int[2];
        int low=0;
        int high=length-1;
        while(low<high){
            if(nums[low]+nums[high]==target){
                ans[0]=low+1;
                ans[1]=high+1;
                break;
            }else if(nums[low]+nums[high]>target){
                high=high-1;
            }else{
                low=low+1;
            }
        }

        return ans;
        
    }
}