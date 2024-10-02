class Solution {
    public void reverse(int low, int high,int []nums){
        while(low<=high){
            int temp=nums[high];
            nums[high]=nums[low];
            nums[low]=temp;
            low=low+1;
            high=high-1;
        }
    }
    public void rotate(int[] nums, int k) {
        int length=nums.length;
        if(k>length){
            k=k%length;
        }
        reverse(0,length-k-1,nums);
        reverse(length-k,length-1,nums);
        reverse(0,length-1,nums);
    }
}