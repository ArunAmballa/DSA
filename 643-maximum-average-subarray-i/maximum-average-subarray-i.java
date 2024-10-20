class Solution {
    public double findMaxAverage(int[] nums, int k) {
        if(nums.length<k){
            return 0.0;
        }
        double maxi=-1000000;
        int sum=0;
        for(int i=0;i<k;i++){
            sum=sum+nums[i];
        }
        maxi=Math.max(maxi,(double)sum/k);
        for(int i=k;i<nums.length;i++){
            sum-=nums[i-k];
            sum+=nums[i];
            maxi=Math.max(maxi,(double)sum/k);
        }
        return maxi;
    }
}