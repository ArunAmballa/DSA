class Solution {
    public int subarraySum(int[] nums, int k) {

        int count=0;
        int prefixSum=0;
        HashMap<Integer,Integer> countMap=new HashMap<>();
        countMap.put(0,1);

        for(int i=0;i<nums.length;i++){
            prefixSum+=nums[i];
            int target=prefixSum-k;
            if(countMap.containsKey(target)){
                count=count+countMap.get(target);
            }
            countMap.put(prefixSum,countMap.getOrDefault(prefixSum,0)+1);
        }

        return count;
        
    }
}