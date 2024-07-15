/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
    let preSum=0
    let ans=-3246826389692868
    for(let i=0;i<nums.length;i++){
        preSum=preSum+nums[i];
        ans=Math.max(ans,preSum)
        if (preSum<0){
            preSum=0
        }
    }
    return ans
};