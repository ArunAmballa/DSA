class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s=0
        e=0
        p=1
        cnt=0
        while e<len(nums):
            p=p*nums[e]
            if p<k:
                cnt=cnt+(e-s+1)
                e=e+1
            else:
                while p>=k and s<=e:
                    p=p/nums[s]
                    s=s+1
                if p<k:
                    cnt=cnt+(e-s+1)
                e=e+1
        return cnt

        