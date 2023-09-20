class Solution:
    def helper(self,bloomDay,p,k,m):
        cnt=0
        groups=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=p:
                cnt=cnt+1
                if cnt==k:
                    groups=groups+1
                    cnt=0
            else:
                cnt=0
        if groups>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        lo=min(bloomDay)
        maxi=max(bloomDay)
        hi=maxi
        ans=maxi
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(bloomDay,mid,k,m)==True:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans

        