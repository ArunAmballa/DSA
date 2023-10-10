#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def get(self,n,i):
        return n&(1<<i)!=0
    def set(self,n,i):
        return n|(1<<i)
    def clear(self,n,i):
        return n&(~(1<<i))
    def bitManipulation(self, n, i):
        a=1 if self.get(n,i-1)==True else 0
        b=self.set(n,i-1)
        c=self.clear(n,i-1)
        print(a,end=" ")
        print(b,end=" ")
        print(c,end=" ")

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, i = list(map(int, input().split()))
        ob = Solution()
        ob.bitManipulation(n, i)
        print()
# } Driver Code Ends