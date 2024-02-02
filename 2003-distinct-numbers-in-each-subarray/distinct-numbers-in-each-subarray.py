class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in range(k):
            d[nums[i]]=d.get(nums[i],0)+1
        ans.append(len(d))
        for i in range(k,len(nums)):
            d[nums[i-k]]=d.get(nums[i-k],0)-1
            if d[nums[i-k]]==0:
                del d[nums[i-k]]
            d[nums[i]]=d.get(nums[i],0)+1
            ans.append(len(d))
        return ans
        