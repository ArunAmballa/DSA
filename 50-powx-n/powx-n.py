class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=abs(n)
        ans=1
        for i in range(0,int(math.log2(n))+1):
            if(n&(1<<i)!=0):
                ans=ans*x
            x=x*x
        return ans
        