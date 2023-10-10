#User function Template for python3

class Solution:
    def XOR(self,n):
        if n%4==0:
            return n
        elif n%4==1:
            return 1
        elif n%4==2:
            return n+1
        else:
            return 0
    def findXOR(self, l, r):
        return self.XOR(r) ^self.XOR(l-1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        l, r = list(map(int, input().split()))
        ob = Solution()
        res = ob.findXOR(l, r)
        print(res)
# } Driver Code Ends