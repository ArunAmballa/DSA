/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let lo=0;
    let hi=nums.length-1
    let ans=Number.MAX_SAFE_INTEGER;
    while(lo<=hi){
        mid=Math.floor((lo+hi)/2)
        if(nums[lo]<=nums[mid]){
            ans=Math.min(ans,nums[lo])
            lo=mid+1
        }else{
            ans=Math.min(ans,nums[mid])
            hi=mid-1
        }
    }
    return ans
    
};