class Solution {
    public int removeDuplicates(int[] nums) {

        int length=nums.length;
        int i=0;
        int j=0;
        while(i<=j && j<length){
            if(nums[j]!=nums[i]){
                int temp=nums[i+1];
                nums[i+1]=nums[j];
                nums[j]=temp;
                i+=1;
                j+=1;
            }else{
                j+=1;
            }
            
            
        }
        return i+1;
        
    }
}