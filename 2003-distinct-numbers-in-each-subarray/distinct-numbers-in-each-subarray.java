class Solution {
    public int[] distinctNumbers(int[] nums, int k) {
        ArrayList<Integer> ans=new ArrayList<>();
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<k;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        ans.add(map.size());
        for(int i=k;i<nums.length;i++){
            map.put(nums[i-k],map.get(nums[i-k])-1);
            if(map.get(nums[i-k])==0){
                map.remove(nums[i-k]);
            }
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            ans.add(map.size());
        }
        int size=ans.size();
        int []finalAnswer=new int[size];
        for(int i=0;i<size;i++){
            finalAnswer[i]=ans.get(i);
        }
        return finalAnswer;
    }
}