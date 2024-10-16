class Solution {
    public int helper(int number){
        for(int i=0;i<32;i++){
            if((number&(1<<i))!=0){
                return i;
            }
        }
        return 0;
    }
    public int[] singleNumber(int[] nums) {
        int xor=0;
        int length=nums.length;
        for(int i=0;i<length;i++){
            xor=xor^nums[i];
        }
        int setBit=helper(xor);
        int one=0;
        int zero=0;
        for(int i=0;i<length;i++){
            if((nums[i]&(1<<setBit))!=0){
                one=one^nums[i];
            }else{
                zero=zero^nums[i];
            }
        }

        return new int[]{zero,one};
    }
}