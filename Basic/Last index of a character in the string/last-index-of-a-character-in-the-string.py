#User function Template for python3

class Solution:
    def recursion(self,s,ind,p):
        if s[ind]==p:
            return ind
        if ind<0:
            return -1
        return self.recursion(s,ind-1,p)
    def LastIndex(self, s, p):
        return self.recursion(s,len(s)-1,p)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
# } Driver Code Ends