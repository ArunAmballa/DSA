#User function Template for python3

class Solution:
    def helper(self,i,j,isTrue,S,m,dp):
        if i>j:
            return 0
        if i==j:
            if isTrue==True:
                return int(S[i]=="T")
            else:
                return int(S[i]=="F")
        if dp[i][j][isTrue]!=-1:
            return dp[i][j][isTrue]
        ans=0
        for k in range(i+1,j):
            LT=self.helper(i,k-1,True,S,m,dp)
            RT=self.helper(k+1,j,True,S,m,dp)
            LF=self.helper(i,k-1,False,S,m,dp)
            RF=self.helper(k+1,j,False,S,m,dp)
            if S[k]=="&":
                if isTrue==True:
                    ans=(ans+((LT*RT)%m))%m
                else:
                    ans=(ans+((LT*RF)%m+(LF*RF)%m+(LF*RT)%m))%m
            elif S[k]=="|":
                if isTrue==False:
                    ans=(ans+((LF*RF)%m))%m
                else:
                    ans=(ans+((LT*RF)%m+(LT*RT)%m+(LF*RT)%m))%m
            else:
                if isTrue==False:
                    ans=(ans+((LT*RT)%m+(LF*RF)%m))%m
                else:
                    ans=(ans+((LT*RF)%m+(LF*RT)%m))%m
        dp[i][j][isTrue]=ans
        return ans
    def countWays(self, N, S):
        m=1003
        dp=[[[-1 for k in range(2)]for j in range(N)]for i in range(N)]
        return self.helper(0,N-1,True,S,m,dp)


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