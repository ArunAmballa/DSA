/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b)=>a-b)
    let ans=[]
    for(let i=0;i<nums.length;i++){
        if(i>0 && nums[i]===nums[i-1]){
            continue
        }
        lo=i+1
        hi=nums.length-1
        while(lo<hi){
            if((nums[i]+nums[lo]+nums[hi])===0){
                ans.push([nums[i],nums[lo],nums[hi]])
                lo=lo+1;
                hi=hi-1;
                while(nums[lo]==nums[lo-1]){
                    lo=lo+1
                }
                while(nums[hi]===nums[hi+1]){
                    hi=hi-1
                }
            }
            else if((nums[i]+nums[lo]+nums[hi])<0){
                lo=lo+1;
            }
            else{
                hi=hi-1
            }
        }
    }

    return ans
    
};