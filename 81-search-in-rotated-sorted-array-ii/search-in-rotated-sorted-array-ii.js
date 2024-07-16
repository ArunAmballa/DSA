/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    let lo=0
    let hi=nums.length-1
    let ans=false
    while(lo<=hi){
        let mid=Math.floor((lo+hi)/2)
        if(nums[mid]===target){
            return true;
        }else if (nums[lo]===nums[mid] && nums[mid]===nums[hi]){
            lo=lo+1
            hi=hi-1
        }else if (nums[lo]<=nums[mid]){
            if(target >=nums[lo] && target <nums[mid]){
                hi=mid-1
            }else{
                lo=mid+1
            }
        }else{
            if(target>= nums[mid] && target<=nums[hi]){
                lo=mid+1
            }else{
                hi=mid-1
            }
        }
    }
    return ans
    
};