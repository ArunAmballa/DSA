import math
class Solution:
    def helper(self,piles,k):
        cnt=0
        for i in range(len(piles)):
            cnt=cnt+(math.ceil(piles[i]/k))
        return cnt
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        ans=max(piles)
        hi=max(piles)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(piles,mid)<=h:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans

        