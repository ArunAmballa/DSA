class Solution {
   
    public boolean check(int[] nums) {

        int length=nums.length;
        int count=0;
        for(int i=0;i<length;i++){
            if(i==length-1){
                if(nums[i]>nums[0]){
                    count+=1;
                }
            }else{
                if(nums[i]>nums[i+1]){
                    count+=1;
                }
            }
        }

        if(count>=2){
            return false;
        }
        return true;
    }
}