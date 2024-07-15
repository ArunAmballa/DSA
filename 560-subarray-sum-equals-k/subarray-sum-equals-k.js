/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let d={0:1}
    let preSum=0
    let count=0
    for(let i=0;i<nums.length;i++){
        preSum=preSum+nums[i]
        target=preSum-k
        if(target in d){
            count=count+d[target]
        }
        if(preSum in d){
            d[preSum]=d[preSum]+1
        }else{
            d[preSum]=1
        }
    }
    return count;
    
};