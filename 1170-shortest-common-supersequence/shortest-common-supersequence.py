class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        x=str1
        y=str2
        dp=[[-1 for j in range(m+1)]for i in range(n+1)]
        for i in range(0,n+1):
            for j in range(0,m+1):
                if i==0 or j==0:
                    dp[i][j]=0
                    continue
                if x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        i=n
        j=m
        l=[]
        while (i>0 and j>0):
            if x[i-1]==y[j-1]:
                l.append(x[i-1])
                i=i-1
                j=j-1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    l.append(y[j-1])
                    j=j-1
                else:
                    l.append(x[i-1])
                    i=i-1
        
        while j>0:
            l.append(y[j-1])
            j=j-1
        while i>0:
            l.append(x[i-1])
            i=i-1
        s=""
        while l:
            curr=l.pop()
            s=s+curr
        return s
        