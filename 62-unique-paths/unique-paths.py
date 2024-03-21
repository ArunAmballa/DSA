class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        prev=[0 for j in range(m)]
        for i in range(0,n):
            temp=[0]*m
            for j in range(0,m):
                if i==0 and j==0:
                    temp[j]=1
                else:
                    top=0
                    left=0
                    if i>=0:
                        top=prev[j]
                    if j>=0:
                        left=temp[j-1]
                    temp[j]=top+left
            prev=temp
        return prev[m-1]
        