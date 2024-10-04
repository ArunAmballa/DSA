class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        int length=nums.length;

        List<List<Integer>> ans=new ArrayList<>();

        for(int i=0;i<length;i++){

            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            
            int low=i+1;
            int high=length-1;

            while(low<high){
                if(nums[low]+nums[high]+nums[i]==0){
                    ArrayList<Integer> list=new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[low]);
                    list.add(nums[high]);
                    ans.add(list);
                    low=low+1;
                    high=high-1;
                    while(low<high && nums[low]==nums[low-1]){
                        low=low+1;
                    }

                    while(low<high && nums[high]==nums[high+1] ){
                        high=high-1;
                    }
                    
                }else if(nums[low]+nums[high]+nums[i]<0){
                    low=low+1;
                }else{
                    high=high-1;
                }
            }
        }

        return ans;
        
    }
}