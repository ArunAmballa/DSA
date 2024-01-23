class Solution:
    def helper(self,bloomDay,day,k,m):
        cnt=0
        boquets=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                cnt=cnt+1
                if cnt==k:
                    boquets=boquets+1
                    cnt=0
            else:
                cnt=0
        if boquets>=m:
            return True
        return False
            
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        lo=min(bloomDay)
        hi=max(bloomDay)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(bloomDay,mid,k,m)==True:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans
        