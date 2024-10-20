class Solution {
    public int longestOnes(int[] nums, int k) {
        int length=nums.length;
        int left=0;
        int right=0;
        int zeroCount=0;
        int maxi=0;
        while(right<length){
            if(nums[right]==0){
                zeroCount++;
            }
            while(zeroCount>k){
                if(nums[left]==0){
                    zeroCount=zeroCount-1;
                }
                left=left+1;
            }
            if(zeroCount<=k){
                maxi=Math.max(maxi,right-left+1);
            }
            right++;
        }
        return maxi; 
    }
}


