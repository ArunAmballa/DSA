class Solution {
    public int missingNumber(int[] nums) {

        int xor1=0;
        int xor2=0;
        int length=nums.length;
        for(int i=0;i<length;i++){
            xor1=xor1^i+1;
            xor2=xor2^nums[i];
        }
        return xor1^xor2;
        
    }
}