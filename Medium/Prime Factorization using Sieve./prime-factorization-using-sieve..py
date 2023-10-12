#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def sieve(self):
        n=2*100000
        self.sieve=[i for i in range(0,(n+1))]
        for i in range(2,int(n**0.5)+1):
            if self.sieve[i]==i:
                j=i*i
                while j<=n:
                    self.sieve[j]=i
                    j=j+i
    
        
    def findPrimeFactors(self, N):
        ans=[]
        while N!=1:
            ans.append(self.sieve[N])
            N=N//self.sieve[N]
        ans.sort()
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    ob = Solution()
    ob.sieve()
    for _ in range (t):
        n = int(input())
        ans = ob.findPrimeFactors(n)
        for v in ans:
            print(v, end = ' ')
        print()
# } Driver Code Ends