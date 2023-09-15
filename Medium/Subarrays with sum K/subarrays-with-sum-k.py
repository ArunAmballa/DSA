#User function Template for python3

class Solution:
    def findSubArraySum(self, arr, N, k):
        
        d={0:1}
        valSum=0
        cnt=0
        for i in range(len(arr)):
            valSum=valSum+arr[i]
            target=valSum-k
            if target in d:
                cnt=cnt+d[target]
            d[valSum]=d.get(valSum,0)+1
        return cnt
            
            
        
              


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends