class Solution:
    def helper(self,weights,mid):
        days=0
        weight=0
        for i in range(len(weights)):
            if weight+weights[i]<=mid:
                weight=weight+weights[i]
            else:
                days=days+1
                weight=weights[i]
        return days+1
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo=max(weights)
        hi=sum(weights)
        ans=hi
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(weights,mid)<=days:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans
        