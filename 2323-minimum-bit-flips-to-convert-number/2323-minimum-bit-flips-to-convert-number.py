class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt=0
        for i in range(0,32):
            if start&(1<<i)==0 and goal&(1<<i)!=0:
                cnt=cnt+1
            elif start&(1<<i)!=0 and goal&(1<<i)==0:
                cnt=cnt+1
        return cnt

        