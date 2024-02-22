class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        lo=0
        hi=len(nums)-1
        while len(nums)!=len(res):
            res.append(nums[lo])
            lo=lo+1
            if lo<hi:
                res.append(nums[hi])
                hi=hi-1
        return res        