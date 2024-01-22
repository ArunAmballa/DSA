import math
class Solution:
    def helper(self,piles,mid):
        ans=0
        for i in range(len(piles)):
            ans=ans+math.ceil(piles[i]/mid)
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=max(piles)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(piles,mid)>h:
                lo=mid+1
            else:
                ans=mid
                hi=mid-1
        return ans

        