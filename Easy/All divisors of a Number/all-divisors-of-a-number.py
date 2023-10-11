#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def print_divisors(self, N):
        ans=[]
        for i in range(1,int(math.sqrt(N))+1):
            k=N//i
            if N%i==0 and N==k*k:
                ans.append(i)
            elif N%i==0:
                ans.append(i)
                ans.append(int(N//i))
        ans.sort()
        for i in ans:
            print(i,end=" ")
            
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends