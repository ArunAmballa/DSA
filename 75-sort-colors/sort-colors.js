/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let lo=0
    let hi=nums.length-1
    let k=0
    while(k<=hi){
        if(nums[k]===0){
            [nums[k],nums[lo]]=[nums[lo],nums[k]]
            lo=lo+1
            k=k+1
        }
        else if (nums[k]==2){
            [nums[hi],nums[k]]=[nums[k],nums[hi]]
            hi=hi-1
        }
        else{
            k=k+1
        }
    }
    
};