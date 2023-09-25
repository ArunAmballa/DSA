class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n=-(n)
            x=1/x
        ans=1
        for i in range(0,int(math.log(n,2))+1):
            if n&(1<<i)!=0:
                ans=ans*x
            x=x*x
        return ans
        