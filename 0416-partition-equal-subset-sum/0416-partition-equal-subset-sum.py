class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        valSum=sum(nums)
        N=len(nums)
        if valSum&1==1:
            return False
        w=valSum//2
        prev=[0]*(w+1)
        curr=[0]*(w+1)
        for i in range(0,N+1):
            for j in range(0,w+1):
                if j==0:
                    prev[j]=True
                    continue
                if i==0:
                    prev[j]=False
                    continue
                if nums[i-1]<=j:
                    curr[j]=prev[j-nums[i-1]] or prev[j]
                else:
                   curr[j]=prev[j]
            prev=curr[:]
        return curr[w]

