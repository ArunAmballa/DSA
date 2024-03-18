#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def helper(self,n,lastPlace,ans,s):
        if n==0:
            ans.append(s)
            return 
        if lastPlace==0:
            self.helper(n-1,0,ans,s+"0")
            self.helper(n-1,1,ans,s+"1")
        else:
            self.helper(n-1,0,ans,s+"0")
        
        
    def generateBinaryStrings(self, n):
        ans=[]
        s=""
        self.helper(n,0,ans,s)
        return ans

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
# } Driver Code Ends