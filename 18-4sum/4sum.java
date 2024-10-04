class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int length=nums.length;

        List<List<Integer>> ans=new ArrayList<>();

        for(int i=0;i<length-3;i++){

            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }

            for(int j=i+1;j<length-2;j++){
                if(j>i+1 && nums[j]==nums[j-1]){
                    continue;
                }

                int low=j+1;
                int high=length-1;

                while(low<high){
                    long sum=(long) nums[i]+nums[j]+nums[low]+nums[high];
                    if(sum==target){
                        List<Integer> list=new ArrayList<>();
                        list.add(nums[i]);
                        list.add(nums[j]);
                        list.add(nums[low]);
                        list.add(nums[high]);
                        ans.add(list);
                        low=low+1;
                        high=high-1;
                        while(low<high && nums[low]==nums[low-1]){
                            low=low+1;
                        }
                        while(low<high && nums[high]==nums[high+1]){
                            high=high-1;
                        }
                    }else if(sum<target){
                        low=low+1;
                    }else{
                        high=high-1;
                    }
                }
            }
        }

        return ans;
        
    }
}