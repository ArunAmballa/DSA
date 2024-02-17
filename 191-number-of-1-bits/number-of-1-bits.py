class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        for i in range(32):
            if n&(1<<i)!=0:
                cnt=cnt+1
        return cnt
            
        