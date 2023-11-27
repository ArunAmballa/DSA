#User function Template for python3

class Solution:
    def helper(self,i,j,s,isTrue,m,dp):
        if i>j:
            return 0
        if i==j:
            if isTrue==True:
                return int(s[i]=="T")
            else:
                return int(s[i]=="F")
        if dp[i][j][isTrue]!=-1:
            return dp[i][j][isTrue]
        ans=0
        for k in range(i+1,j,2):
            lf=self.helper(i,k-1,s,False,m,dp)
            lt=self.helper(i,k-1,s,True,m,dp)
            rf=self.helper(k+1,j,s,False,m,dp)
            rt=self.helper(k+1,j,s,True,m,dp)
            if s[k]=="&":
                if isTrue==True:
                    ans=(ans+(lt*rt)%m)%m
                else:
                    ans=(ans+(lf*rf)%m +(lt*rf)%m +(lf*rt)%m)%m
            if s[k]=="^":
                if isTrue==True:
                    ans=(ans+(lf*rt)%m +(lt*rf)%m)%m
                else:
                    ans=(ans+(lt*rt)%m+(lf*rf)%m)%m
            if s[k]=="|":
                if isTrue==True:
                    ans=(ans+(lf*rt)%m+(lt*rf)%m+(lt*rt)%m)%m
                else:
                    ans=(ans+(lf*rf)%m)%m
        dp[i][j][isTrue]=ans
        return dp[i][j][isTrue]
    def countWays(self, N, S):
        dp=[[[-1 for k in range(2)]for j in range(N)]for i in range(N)]
        return self.helper(0,N-1,S,True,1003,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends