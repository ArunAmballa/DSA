class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=-1*n
            x=1.0/x
        if n==0:
            return 1
        ans=1
        for i in range(0,int(math.log(n,2))+1):
            if n&(1<<i)!=0:
                ans=ans*x
            x=x*x
        return ans if n>0 else 1/ans
        