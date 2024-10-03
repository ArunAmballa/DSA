class Solution {
    public int[] twoSum(int[] nums, int target) {
        int []ans=new int[2];
        HashMap<Integer,Integer> map=new HashMap<>();
        int length=nums.length;
        for(int i=0;i<length;i++){
            int a=target-nums[i];
            if(map.containsKey(a)){
                ans[0]=map.get(a);
                ans[1]=i;
                return ans;
            }
            map.put(nums[i],i);
        }
        return ans;
        
    }
}