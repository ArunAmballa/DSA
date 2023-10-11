class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        primes=[0]*(n)
        primes[0]=-1
        primes[1]=-1
        for i in range(2,int(math.sqrt(n))+1):
            if primes[i]==0:
                j=i*i
                while j<n:
                    primes[j]=-1
                    j=j+i
        cnt=0
        for i in range(len(primes)):
            if primes[i]==0:
                cnt=cnt+1
        return cnt        