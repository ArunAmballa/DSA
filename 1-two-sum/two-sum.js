/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let d={}
    for(let i=0;i<nums.length;i++){
        let b=target-nums[i]
        if( b in d){
            return [d[b],i]
        }else{
            d[nums[i]]=i
        }

    }
    
};