#User function Template for python3

class Solution:
    def factorSum(self, N):
        valSum=0
        for i in range(1,int(N**0.5)+1):
            if N%i==0 and i==(N//i):
                valSum=valSum+i
            elif N%i==0:
                valSum=valSum+i+(N//i)
        return valSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.factorSum(N))
# } Driver Code Ends