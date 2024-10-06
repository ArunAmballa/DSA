class Solution {

    public int findMax(int []nums){
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            maxi=Math.max(maxi,nums[i]);
        }
        return maxi;
    }

    public int findSum(int []nums){
        int sum=0;
        for(int i=0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        return sum;
    }
    public int helper(int []nums,int maximumSubArraySum){
        int subArraySum=0;
        int numberOfSubarray=0;
        for(int i=0;i<nums.length;i++){
            subArraySum=subArraySum+nums[i];
            if(subArraySum>maximumSubArraySum){
                numberOfSubarray+=1;
                subArraySum=nums[i];
            }
        }
        return numberOfSubarray+1;
    }
    public int splitArray(int[] nums, int k) {
        
        int low=findMax(nums);
        int high=findSum(nums);
        int ans=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            int numberOfSubArrays=helper(nums,mid);
            if(numberOfSubArrays<=k){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }

        return ans;
    }
}