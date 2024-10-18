class Solution {
    public int[] twoSum(int[] nums, int target) {

        int length=nums.length;

        int [][]temp=new int[length][2];

        int []ans=new int[2];

        for(int i=0;i<length;i++){
            temp[i][0]=nums[i];
            temp[i][1]=i;
        }

        Arrays.sort(temp,(a,b)->Integer.compare(a[0],b[0]));

        int low=0;
        int high=length-1;
        while(low<high){
            if(temp[low][0]+temp[high][0]==target){
                ans[0]=temp[low][1];
                ans[1]=temp[high][1];
                break;
            }else if(temp[low][0]+temp[high][0]<target){
                low=low+1;
            }else{
                high=high-1;
            }
        }

        return ans;
    }

}




