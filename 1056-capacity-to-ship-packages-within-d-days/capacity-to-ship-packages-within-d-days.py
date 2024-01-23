class Solution:
    def helper(self,weights,allowed):
        days=0
        weightSum=0
        for i in range(len(weights)):
            if weightSum+weights[i]<=allowed:
                weightSum=weightSum+weights[i]
            else:
                days=days+1
                weightSum=weights[i]
        return days+1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo=max(weights)
        hi=sum(weights)
        ans=-(1<<31)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(weights,mid)<=days:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans
            

        