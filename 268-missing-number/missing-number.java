class Solution {
    public int missingNumber(int[] nums) {

        int length=nums.length;
        int sum=(length*(length+1))/2;
        int arraySum=0;
        for(int i=0;i<length;i++){
            arraySum+=nums[i];
        }
        return sum-arraySum;
        
    }
}