class Solution {
     public void merge(int low, int mid,int high,int []nums){
        int i=low;
        int j=mid+1;
        ArrayList<Integer> temp=new ArrayList<>();

        while(i<=mid && j<=high){
            if(nums[i]<nums[j]){
                temp.add(nums[i]);
                i++;
            }else{
                temp.add(nums[j]);
                j++;
            }
        }

        while(i<=mid){
            temp.add(nums[i]);
            i++;
        }

        while(j<=high){
            temp.add(nums[j]);
            j++;
        }

        for(int k=low;k<=high;k++){
            nums[k]=temp.get(k-low);
        }
    }

    public void mergeSorted(int low,int high, int []nums){
        if(low>=high){
            return ;
        }
        int mid=(low+high)/2;
        mergeSorted(low,mid,nums);
        mergeSorted(mid+1,high,nums);
        merge(low,mid,high,nums);

    }
    public int[] sortArray(int[] nums) {

        mergeSorted(0,nums.length-1,nums);
        return nums;
        
    }
}