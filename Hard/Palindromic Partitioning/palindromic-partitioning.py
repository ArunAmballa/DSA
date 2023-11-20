#User function Template for python3

class Solution:
    def isPalindrome(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True
    def helper(self,i,n,s,dp):
        if i==n-1:
            return 0
        if self.isPalindrome(s,i,n-1):
            return 0
        if dp[i]!=-1:
            return dp[i]
        ans=1<<31
        for j in range(i,n):
            if self.isPalindrome(s,i,j):
                cost=1+self.helper(j+1,n,s,dp)
                ans=min(ans,cost)
        dp[i]=ans
        return dp[i]
    def palindromicPartition(self, s):
        dp=[-1 for j in range(len(s))]
        return self.helper(0,len(s),s,dp)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends