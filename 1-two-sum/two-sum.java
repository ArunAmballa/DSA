class Solution {
    public int[] twoSum(int[] nums, int target) {

        int []ans=new int[2];
        int length=nums.length;
        int [][]eleIndex=new int[length][2];

        for(int i=0;i<length;i++){
            eleIndex[i][0]=nums[i];
            eleIndex[i][1]=i;
        }
        Arrays.sort(eleIndex,(a,b)->Integer.compare(a[0],b[0]));
        int low=0;
        int high=length-1;

        while(low<=high){
            if(eleIndex[low][0]+eleIndex[high][0]==target){
                ans[0]=eleIndex[low][1];
                ans[1]=eleIndex[high][1];
                return ans;
            }else if(eleIndex[low][0]+eleIndex[high][0]<target){
                low=low+1;
            }else{
                high=high-1;
            }
        }

        return ans;
    }
}


